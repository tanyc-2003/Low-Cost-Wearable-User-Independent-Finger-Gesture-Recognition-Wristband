%% Classes
%(1) Cylindrical: for holding cylindrical tools
%(2) Hook: for supporting a heavy load
%(3) Tip: for holding small tools
%(4) Palmar: for grasping with palm facing the object
%(5) Spherical: for holding spherical tools
%(6) Lateral: for holding thin, flat objects

close all
clear
clc

%% Load data
data1 = load('female_1.mat');
data2 = load('female_2.mat');
data3 = load('female_3.mat');
data4 = load('male_1.mat');
data5 = load('male_2.mat');


%% Preparing data
cyl_female1 = (data1.cyl_ch1 - data1.cyl_ch2);
hook_female1 = (data1.hook_ch1 - data1.hook_ch2);
tip_female1 = (data1.tip_ch1 - data1.tip_ch2);
palm_female1 = (data1.palm_ch1 - data1.palm_ch2);
spher_female1 = (data1.spher_ch1 - data1.spher_ch2);
lat_female1 = (data1.lat_ch1 - data1.lat_ch2);

cyl_female2 = (data2.cyl_ch1 - data2.cyl_ch2);
hook_female2 = (data2.hook_ch1 - data2.hook_ch2);
tip_female2 = (data2.tip_ch1 - data2.tip_ch2);
palm_female2 = (data2.palm_ch1 - data2.palm_ch2);
spher_female2 = (data2.spher_ch1 - data2.spher_ch2);
lat_female2 = (data2.lat_ch1 - data2.lat_ch2);

cyl_female3 = (data3.cyl_ch1 - data3.cyl_ch2);
hook_female3 = (data3.hook_ch1 - data3.hook_ch2);
tip_female3 = (data3.tip_ch1 - data3.tip_ch2);
palm_female3 = (data3.palm_ch1 - data3.palm_ch2);
spher_female3 = (data3.spher_ch1 - data3.spher_ch2);
lat_female3 = (data3.lat_ch1 - data3.lat_ch2);

cyl_male1 = (data4.cyl_ch1 - data4.cyl_ch2);
hook_male1 = (data4.hook_ch1 - data4.hook_ch2);
tip_male1 = (data4.tip_ch1 - data4.tip_ch2);
palm_male1 = (data4.palm_ch1 - data4.palm_ch2);
spher_male1 = (data4.spher_ch1 - data4.spher_ch2);
lat_male1 = (data4.lat_ch1 - data4.lat_ch2);

cyl_male2 = (data5.cyl_ch1 - data5.cyl_ch2);
hook_male2 = (data5.hook_ch1 - data5.hook_ch2);
tip_male2 = (data5.tip_ch1 - data5.tip_ch2);
palm_male2 = (data5.palm_ch1 - data5.palm_ch2);
spher_male2 = (data5.spher_ch1 - data5.spher_ch2);
lat_male2 = (data5.lat_ch1 - data5.lat_ch2);

%% Type:
%       1 - test was performed using each subject at its own control, i.e., 
%           the data coming from each subject were not mixed with data coming 
%           from any other subject.
%       2 - mixing the individual data of each subject forming a single dataset.
%       3 - only two classes: power grasp and precision grasp.
type = 2;

if type == 1
    % here it is necessary to change the test subject: female1, male1, etc... 
    X = [cyl_female1;
        hook_female1;
        tip_female1;
        palm_female1;
        spher_female1;
        lat_female1];
    
    Y(1:30,1) = 1;
    Y(31:60,1) = 2;
    Y(61:90,1) = 3;
    Y(91:120,1) = 4;
    Y(121:150,1) = 5;
    Y(151:180,1) = 6;
end
if type == 2
    X = [cyl_female1; cyl_female2; cyl_female3; cyl_male1; cyl_male2;...
        hook_female1; hook_female2; hook_female3; hook_male1; hook_male2;...
        tip_female1; tip_female2; tip_female3; tip_male1; tip_male2; ...
        palm_female1; palm_female2; palm_female3; palm_male1; palm_male2;...
        spher_female1; spher_female2; spher_female3; spher_male1; spher_male2;...
        lat_female1; lat_female2; lat_female3; lat_male1; lat_male2];
    
    Y(1:150,1) = 1;
    Y(151:300,1) = 2;
    Y(301:450,1) = 3;
    Y(451:600,1) = 4;
    Y(601:750,1) = 5;
    Y(751:900,1) = 6;
    
end
if type == 3
    X = [cyl_female1; cyl_female2; cyl_female3; cyl_male1; cyl_male2;...
        hook_female1; hook_female2; hook_female3; hook_male1; hook_male2;...
        tip_female1; tip_female2; tip_female3; tip_male1; tip_male2; ...
        palm_female1; palm_female2; palm_female3; palm_male1; palm_male2;...
        spher_female1; spher_female2; spher_female3; spher_male1; spher_male2;...
        lat_female1; lat_female2; lat_female3; lat_male1; lat_male2];
    
    
    Y(1:150,1) = 1;
    Y(151:300,1) = 1;
    Y(301:450,1) = 2;
    Y(451:600,1) = 2;
    Y(601:750,1) = 1;
    Y(751:900,1) = 2;
end

wv = 'db10'; %wavelet family

%% 5 by 2 CV
seeds = [13 51 137 24659 347];

for i = 1:length(seeds)
    
    rng(seeds(i));
    cv = cvpartition(Y,'kfold',2);
    
    for j = 1:cv.NumTestSets
    
        Xtr = X(cv.training(j),:);
        Ytr = Y(cv.training(j));
        Xts = X(cv.test(j),:);
        Yts = Y(cv.test(j));
        
        %% Train
        [mx,my] = size(Xtr);
        
        for k=1:mx
            ch_tr = Xtr(k,:);
            if(~isnan(ch_tr))
                dwt = modwt(ch_tr,wv);
                kurt = kurtosis(ch_tr);
                skew = skewness(ch_tr);
                vari = var(ch_tr);
                zcd = length(zerocross(ch_tr));
                %iemg = trapz(abs(ch_tr))/length(ch_tr);
                energy_by_scales = sum(dwt.^2,2);
                stdv = std(dwt')';
                Xtrain(:,k) = [energy_by_scales; kurt; skew; vari; zcd; stdv];
            end
        end
        
        %% Test
        [nx,ny] = size(Xts);
        
        for k=1:nx
            ch_ts = Xts(k,:);
            if(~isnan(ch_ts))
                dwt = modwt(ch_ts,wv);
                kurt = kurtosis(ch_ts);
                skew = skewness(ch_ts);
                vari = var(ch_ts);
                zcd = length(zerocross(ch_ts));
                %iemg = trapz(abs(ch_tr))/length(ch_tr);
                energy_by_scales = sum(dwt.^2,2);
                stdv = std(dwt')';
                Xtest(:,k) = [energy_by_scales; kurt; skew; vari; zcd; stdv];
            end
        end
        
        %% Autoencoder Parameters
        % Network Struct
        hiddenSize1 = 1105;
        autoenc1 = trainAutoencoder(Xtrain,hiddenSize1, ...
            'MaxEpochs',100, ...
            'L2WeightRegularization',0.004, ...
            'SparsityRegularization',8, ...
            'SparsityProportion',0.15, ...
            'DecoderTransferFunction', 'logsig', ...
            'ScaleData', false);
        
        features1 = encode(autoenc1,Xtrain);
        
        Ytrain = full(ind2vec(Ytr'));
        
        % Softmax layer train
        softnet = trainSoftmaxLayer(features1,Ytrain,'MaxEpochs',1000);
        
        % Stacking
        deepnet = stack(autoenc1,softnet);
        deepnet = train(deepnet,Xtrain,Ytrain);
        
        label_deep = vec2ind(deepnet(Xtest));
        label_prob = deepnet(Xtest);
        AccRate_deep(i,j) = sum(Yts' == label_deep)/length(Yts);
        C_deep{i,j} = confusionmat(Yts,label_deep);
        
        %% KNN
        KNN = fitcknn(Xtrain',Ytr,'NumNeighbors',5);
        label_knn = predict(KNN,Xtest');
        AccRate_knn(i,j) = sum(Yts == label_knn)/length(Yts);
        C_knn{i,j} = confusionmat(Yts,label_knn);
        
        %% SVM
        tSVM = templateSVM('Standardize',1,'KernelFunction','linear');
        SVM = fitcecoc(Xtrain',Ytr,'Learners',tSVM);
        label_svm = predict(SVM,Xtest');
        AccRate_svm(i,j) = sum(Yts == label_svm)/length(Yts);
        C_svm{i,j} = confusionmat(Yts,label_svm);
        
        %% LDA
        LDA = fitcdiscr(Xtrain',Ytr);
        label_lda = predict(LDA,Xtest');
        AccRate_lda(i,j) = sum(Yts == label_lda)/length(Yts);
        C_lda{i,j} = confusionmat(Yts,label_lda);
    end
end

%% Accuracy
mean(AccRate_deep(:))
SEM_deep = std(AccRate_deep(:))/sqrt(length(AccRate_deep(:))); % Standard Error
ts_deep = tinv([0.025  0.975],length(AccRate_deep(:))-1);      % T-Score
CI_deep = mean(AccRate_deep(:)) + ts_deep*SEM_deep;
(ts_deep*SEM_deep)*100

mean(AccRate_knn(:))
SEM_knn = std(AccRate_knn(:))/sqrt(length(AccRate_knn(:)));  % Standard Error
ts_knn = tinv([0.025  0.975],length(AccRate_knn(:))-1);      % T-Score
CI_knn = mean(AccRate_knn(:)) + ts_knn*SEM_knn;
ts_knn*SEM_knn*100

mean(AccRate_svm(:))
SEM_svm = std(AccRate_svm(:))/sqrt(length(AccRate_svm(:)));  % Standard Error
ts_svm = tinv([0.025  0.975],length(AccRate_svm(:))-1);      % T-Score
CI_svm = mean(AccRate_svm(:)) + ts_svm*SEM_svm;
ts_svm*SEM_svm*100

mean(AccRate_lda(:))
SEM_lda = std(AccRate_lda(:))/sqrt(length(AccRate_lda(:)));  % Standard Error
ts_lda = tinv([0.025  0.975],length(AccRate_lda(:))-1);      % T-Score
CI_lda = mean(AccRate_lda(:)) + ts_lda*SEM_lda;
ts_lda*SEM_lda*100

%% Get Statistical Results
%(1) Cylindrical: for holding cylindrical tools
%(2) Hook: for supporting a heavy load
%(3) Tip: for holding small tools
%(4) Palmar: for grasping with palm facing the object
%(5) Spherical: for holding spherical tools
%(6) Lateral: for holding thin, flat objects

[row,col] = size(C_deep{1,1});

confMatrix_deep = zeros(row,col);
confMatrix_svm = zeros(row,col);
confMatrix_lda = zeros(row,col);
confMatrix_knn = zeros(row,col);

for i = 1:5
    for j = 1:2
        confMatrix_deep = confMatrix_deep + C_deep{i,j};
        confMatrix_svm = confMatrix_svm + C_svm{i,j};
        confMatrix_lda = confMatrix_lda + C_lda{i,j};
        confMatrix_knn = confMatrix_knn + C_knn{i,j};
    end
end

[result_deep,reference_deep]= getStatistical(confMatrix_deep);
[result_svm,reference_svm]= getStatistical(confMatrix_svm);
[result_lda,reference_lda]= getStatistical(confMatrix_lda);
[result_knn,reference_knn]= getStatistical(confMatrix_knn);

% figure
% ylabel('Amplitude [V]')
% ax1 = subplot(4,1,1);
% plot(ch_ts)
% title(ax1,'Raw EMG Signal')
% ylabel(ax1,'Amplitude [V]')
% 
% ax2 = subplot(4,1,2);
% plot(dwt(1,:))
% title(ax2,'First MODWT sub-band')
% ylabel(ax2,'Amplitude [V]')
% 
% ax3 = subplot(4,1,3);
% plot(dwt(3,:))
% title(ax3,'Third MODWT sub-band')
% ylabel(ax3,'Amplitude [V]')
% 
% ax4 = subplot(4,1,4);
% plot(dwt(6,:))
% title(ax4,'6th MODWT sub-band')
% ylabel(ax4,'Amplitude [V]')
% 
% xlabel('samples')