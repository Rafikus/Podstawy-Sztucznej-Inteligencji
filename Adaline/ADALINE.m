clear
clc
close all
LitA=[  
    0 1 1 1 0
    1 0 0 0 1
    1 1 1 1 1
    1 0 0 0 1
    1 0 0 0 1];
    
LitB=[  
    1 1 1 1 0
    1 0 0 0 1
    1 1 1 1 0
    1 0 0 0 1
    1 1 1 1 0];
    
LitC=[  
    0 1 1 1 1
    1 0 0 0 0
    1 0 0 0 0
    1 0 0 0 0
    0 1 1 1 1];

LitD=[  
    1 1 1 1 0
    1 0 0 0 1
    1 0 0 0 1
    1 0 0 0 1
    1 1 1 1 0];

LitE=[  
    1 1 1 1 1
    1 0 0 0 0
    1 1 1 1 0
    1 0 0 0 0
    1 1 1 1 1];

LitF=[  
    1 1 1 1 1
    1 0 0 0 0
    1 1 1 1 0
    1 0 0 0 0
    1 0 0 0 0];

LitG=[  
    0 1 1 1 1
    1 0 0 0 0
    1 0 1 1 1
    1 0 0 0 1
    0 1 1 1 0];

LitH=[  
    1 0 0 0 1
    1 0 0 0 1
    1 1 1 1 1
    1 0 0 0 1
    1 0 0 0 1];

LitI=[  
    0 0 1 0 0
    0 0 1 0 0
    0 0 1 0 0
    0 0 1 0 0
    0 0 1 0 0];

LitJ=[  
    0 1 1 1 1
    0 0 0 0 1
    0 0 0 0 1
    0 0 0 0 1
    0 1 1 1 0];

LitK=[  
    1 0 0 1 0
    1 0 1 0 0
    1 1 0 0 0
    1 0 1 0 0
    1 0 0 1 0];

LitL=[  
    1 0 0 0 0
    1 0 0 0 0
    1 0 0 0 0
    1 0 0 0 0
    1 1 1 1 1];

LitM=[  
    1 1 0 1 1
    1 0 1 0 1
    1 0 1 0 1
    1 0 0 0 1
    1 0 0 0 1];

LitN=[  
    1 0 0 0 1
    1 1 0 0 1
    1 0 1 0 1
    1 0 0 1 1
    1 0 0 0 1];

LitO=[  
    0 1 1 1 0
    1 0 0 0 1
    1 0 0 0 1
    1 0 0 0 1
    0 1 1 1 0];

LitP=[  
    1 1 1 1 0
    1 0 0 0 1
    1 1 1 1 0
    1 0 0 0 0
    1 0 0 0 0];

LitR=[  
    1 1 1 1 0
    1 0 0 0 1
    1 1 1 1 0
    1 0 0 0 1
    1 0 0 0 1];

LitS=[  
    0 1 1 1 1
    1 0 0 0 0
    0 1 1 1 0
    0 0 0 0 1
    1 1 1 1 0];

LitT=[  
    1 1 1 1 1
    0 0 1 0 0
    0 0 1 0 0
    0 0 1 0 0
    0 0 1 0 0];
LitU=[  
    1 0 0 0 1
    1 0 0 0 1
    1 0 0 0 1
    1 0 0 0 1
    0 1 1 1 0];

LitW=[  
    1 0 0 0 1
    1 0 0 0 1
    1 0 1 0 1
    1 0 1 0 1
    0 1 0 1 0];

LitX=[  
    1 0 0 0 1
    0 1 0 1 0
    0 0 1 0 0
    0 1 0 1 0
    1 0 0 0 1];

LitY=[  
    1 0 0 0 1
    0 1 0 1 0
    0 0 1 0 0
    0 0 1 0 0
    0 0 1 0 0];

LitZ=[  
    1 1 1 1 1
    0 0 0 1 0
    0 0 1 0 0
    0 1 0 0 0
    1 1 1 1 1];

TA=reshape(LitA,[25 1]);
TB=reshape(LitB,[25 1]);
TC=reshape(LitC,[25 1]);
TD=reshape(LitD,[25 1]);
TE=reshape(LitE,[25 1]);
TF=reshape(LitF,[25 1]);
TG=reshape(LitG,[25 1]);
TH=reshape(LitH,[25 1]);
TI=reshape(LitI,[25 1]);
TJ=reshape(LitJ,[25 1]);
TK=reshape(LitK,[25 1]);
TL=reshape(LitL,[25 1]);
TM=reshape(LitM,[25 1]);
TN=reshape(LitN,[25 1]);
TO=reshape(LitO,[25 1]);
TP=reshape(LitP,[25 1]);
TR=reshape(LitR,[25 1]);
TS=reshape(LitS,[25 1]);
TT=reshape(LitT,[25 1]);
TU=reshape(LitU,[25 1]);
TW=reshape(LitW,[25 1]);
TX=reshape(LitX,[25 1]);
TY=reshape(LitY,[25 1]);
TZ=reshape(LitZ,[25 1]);

T = horzcat(TA, TB, TC, TD, TE, TF, TG, TH, TI, TJ, TK, TL, TM, TN, TO, TP, TR, TS, TT, TU, TW, TX, TY, TZ);

net = newhop(T);
view(net)
W = net.LW{1,1};
b = net.b{1,1};

Lit1=[  1 0 0 0 0
        1 0 0 0 1
        1 0 1 0 1
        1 0 1 0 1
        0 1 0 1 0]

 T1=reshape(Lit1,[25,1]);

 [odpY] = sim(net,1,[],T1);

 odpNN = reshape(odpY,[5 5])

 for i=1:5
    for j=1:5
        if (odpNN(i,j)<1 & odpNN(i,j) >=0.5)
            odpNN(i,j) = 1
        elseif (odpNN(i,j) < 0.5)
            odpNN(i,j) = 0;
    end
 end
 end

 odpNN