function realTimeSVMprediction()

    % Load the trained model
    loadedModel = load('trainedSVMmodel.mat');
    SVM = loadedModel.SVM;
    wv = 'db10';



    % UART Configuration
    portName = 'COM4'; 
    baudRate = 115200; 
    numSamples = 250*3; 
    
    try
        
        % Create serial port object
        s = serialport(portName, baudRate);
        configureTerminator(s, "LF");
        
        fprintf('=== Real-time SVM Prediction Started ===\n');
        fprintf('Waiting for data from %s...\n', portName);

        while true
            flush(s); % Clear any old data

            write(s, 'a', "uint8");

            while true
                if s.NumBytesAvailable > 0
                    line = readline(s); % Read a line
                    
                    % Check for termination signal
                    if strcmp(strtrim(line), "DONE")
                
                        % Now read the actual data
                        rawBytes = read(s, numSamples*2, 'uint8');
                        rawData = typecast(uint8(rawBytes), 'uint16');
            
                        fprintf('%d ',rawData);
                        fprintf('\n');
                        
                        
                        % Get current timestamp
                        currentTime = datetime('now', 'Format', 'HH:mm:ss.SSS');
                        
                        % Process the sample
                        if ~isnan(rawData)
                            % Convert to double if needed
                            sample = double(rawData);
                            
                            % Feature extraction (same as your training pipeline)
                            dwt = modwt(sample, wv);
                            kurt = kurtosis(sample);
                            skew = skewness(sample);
                            vari = var(sample);
                            mav = mean(abs(sample));
                            energy_by_scales = sum(dwt.^2, 2);
                            stdv = std(dwt')';
                            
                            features = [energy_by_scales; kurt; skew; vari; mav; stdv]';
                            fprintf('\nFinal Feature Vector (1x%d):\n', length(features));
                            fprintf('%d ',features);
                            fprintf('\n');
                            
                            
                            % Make prediction
                            predictedClass = predict(SVM, features);


                            % Print to terminal
                            fprintf('[%s] Predicted class: %d --> ', char(currentTime), predictedClass);
                            

                            % Create a persistent figure (won't flicker with updates)
                            if ~isempty(findobj('Type', 'Figure', 'Name', 'Gesture Output'))
                                fig = findobj('Type', 'Figure', 'Name', 'Gesture Output');
                                clf(fig); % Clear existing content
                            else
                                fig = figure('Name', 'Gesture Output', 'NumberTitle', 'off');
                            end
                                                    
                            % Set up the figure
                            set(fig, 'Position', [500 200 600 400], 'Color', [0.1 0.1 0.1]);
                            
                                                        
                            switch predictedClass
                                case 1
                                    fprintf('Thumb\n');
                                    gesture = 'THUMB';
                                case 2
                                    fprintf('Index\n');
                                    gesture = 'INDEX';
                                case 3
                                    fprintf('Middle\n'); 
                                    gesture = 'MIDDLE';
                                case 4
                                    fprintf('Ring\n'); 
                                    gesture = 'RING';
                                case 5
                                    fprintf('Pinky\n'); 
                                    gesture = 'PINKY';
                                case 6
                                    fprintf('Point\n'); 
                                    gesture = 'POINT';
                                case 7
                                    fprintf('Rest\n'); 
                                    gesture = 'REST';
                                otherwise
                                    fprintf('Unknown class: %d\n', predictedClass);  % Handle unexpected values
                                    gesture = 'UNKNOWN';
                            end

                            text(0.5, 0.5, gesture, ...
                            'FontSize', 72, ...
                            'FontWeight', 'bold', 'HorizontalAlignment', 'center');
                        
                            % Force immediate update
                            drawnow;

                            break;

                        end
                    end
                end
            end
        end
        
    catch ME
        fprintf('Error: %s\n', ME.message);
    end
    
    % Clean up
    if exist('s', 'var')
        clear s;
    end
    fprintf('=== Prediction Stopped ===\n');
end