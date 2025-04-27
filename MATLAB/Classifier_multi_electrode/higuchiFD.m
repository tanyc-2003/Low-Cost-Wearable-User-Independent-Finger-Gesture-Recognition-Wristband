function hfd = higuchiFD(signal, kMax)
    % Computes the Higuchi Fractal Dimension (HFD) of a 1D signal.
    % signal - input time series (vector)
    % kMax - maximum segment length (default: 10)

    if nargin < 2
        kMax = 10; % Default value
    end

    N = length(signal);
    Lmk = zeros(kMax, 1);

    for k = 1:kMax
        Lm = zeros(k, 1);
        for m = 1:k
            % Construct subsequence
            idx = m:k:N;
            if length(idx) > 1
                Lm(m) = sum(abs(diff(signal(idx)))) / ((N - 1) / k);
            end
        end
        Lmk(k) = mean(Lm) * (N - 1) / k;
    end

    % Fit log-log curve to get fractal dimension
    kVals = 1:kMax;
    logLmk = log(Lmk);
    logk = log(1 ./ kVals);
    p = polyfit(logk, logLmk', 1);
    hfd = abs(p(1));  % Higuchi Fractal Dimension
end
