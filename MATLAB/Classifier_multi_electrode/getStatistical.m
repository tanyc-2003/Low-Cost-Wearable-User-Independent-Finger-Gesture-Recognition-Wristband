function  [Result,RefereceResult]= getStatistical(c_matrix)
%%
%Finding
%1.TP-True Positive
%2.FP-False Positive
%3.FN-False Negative
%4.TN-True Negative
if (nargin < 1)
    error('Not enough input arguments. Need atleast two vectors as input');
elseif (nargin > 1)
    error('Too many input arguments.');
end
[row,col]=size(c_matrix);
if row~=col
    error('Confusion matrix dimention is wrong')
end
n_class=row;
switch n_class
    case 2
        TP=c_matrix(1,1);
        FN=c_matrix(1,2);
        FP=c_matrix(2,1);
        TN=c_matrix(2,2);
        
    otherwise
        TP=zeros(1,n_class);
        FN=zeros(1,n_class);
        FP=zeros(1,n_class);
        TN=zeros(1,n_class);
        for i=1:n_class
            TP(i)=c_matrix(i,i);
            FN(i)=sum(c_matrix(i,:))-c_matrix(i,i);
            FP(i)=sum(c_matrix(:,i))-c_matrix(i,i);
            TN(i)=sum(c_matrix(:))-TP(i)-FP(i)-FN(i);
            %TN(i)=sum(c_matrix(:))-TP(i);
        end 
end

%%
%Calulations
%1.P-Positive
%2.N-Negative
%3.accuracy
%4.error
%5.Sensitivity (Recall or True positive rate)
%6.Specificity
%7.Precision
%8.FPR-False positive rate
%9.F_score
%10.MCC-Matthews correlation coefficient
%11.kappa-Cohen's kappa
P=TP+FN;
N=FP+TN;
switch n_class
    case 2
        accuracy=(TP+TN)/(P+N);
        Error=1-accuracy;
        Result.Accuracy=(accuracy);
        Result.Error=(Error);
    otherwise
        accuracy=(TP)./(P+N);
        Error=(FP)./(P+N);
        Result.Accuracy=sum(accuracy);
        Result.Error=sum(Error);
end
%RefereceResult.AccuracyOfSingle=(TP ./ P)';
RefereceResult.AccuracyOfSingle=((TP+TN) ./ (P+N))';
RefereceResult.ErrorOfSingle=1-RefereceResult.AccuracyOfSingle;
Sensitivity=TP./P;
Specificity=TN./N;
Precision=TP./(TP+FP);
FPR=1-Specificity;
beta=1;
F1_score=( (1+(beta^2))*(Sensitivity.*Precision) ) ./ ( (beta^2)*(Precision+Sensitivity) );
MCC=[( TP.*TN - FP.*FN ) ./ ( ( (TP+FP).*P.*N.*(TN+FN) ).^(0.5) );...
    ( FP.*FN - TP.*TN ) ./ ( ( (TP+FP).*P.*N.*(TN+FN) ).^(0.5) )] ;
MCC=max(MCC);

%Kappa Calculation BY 2x2 Matrix Shape
pox=sum(accuracy);
Px=sum(P);TPx=sum(TP);FPx=sum(FP);TNx=sum(TN);FNx=sum(FN);Nx=sum(N);
pex=( (Px.*(TPx+FPx))+(Nx.*(FNx+TNx)) ) ./ ( (TPx+TNx+FPx+FNx).^2 );
kappa_overall=([( pox-pex ) ./ ( 1-pex );( pex-pox ) ./ ( 1-pox )]);
kappa_overall=max(kappa_overall);

%Kappa Calculation BY n_class x n_class Matrix Shape
po=accuracy;
pe=( (P.*(TP+FP))+(N.*(FN+TN)) ) ./ ( (TP+TN+FP+FN).^2 );
kappa=([( po-pe ) ./ ( 1-pe );( pe-po ) ./ ( 1-po )]);
kappa=max(kappa);


%%
%Output Struct for individual Classes
%  RefereceResult.Class=class_ref;
RefereceResult.AccuracyInTotal=accuracy';
RefereceResult.ErrorInTotal=Error';
RefereceResult.Sensitivity=Sensitivity';
RefereceResult.Specificity=Specificity';
RefereceResult.Precision=Precision';
RefereceResult.FalsePositiveRate=FPR';
RefereceResult.F1_score=F1_score';
RefereceResult.MatthewsCorrelationCoefficient=MCC';
RefereceResult.Kappa=kappa';
RefereceResult.TruePositive=TP';
RefereceResult.FalsePositive=FP';
RefereceResult.FalseNegative=FN';
RefereceResult.TrueNegative=TN';

%Output Struct for over all class lists
Result.Sensitivity=mean(Sensitivity);
Result.Specificity=mean(Specificity);
Result.Precision=mean(Precision);
Result.FalsePositiveRate=mean(FPR);
Result.F1_score=mean(F1_score);
Result.MatthewsCorrelationCoefficient=mean(MCC);
Result.Kappa=kappa_overall;