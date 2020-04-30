file1 = 'yalefaces';
file = dir(file1);
files = file(~[file.isdir]);


exp_images = zeros(243*320,11,15);
m = 2;
for i = 1:15
    for j = 1:6
         im = imread(fullfile(file1,files(m).name));
         exp_images(:,j,i) = reshape(im,[],1);
         m = m+1;
    end 
end
for i = 1:15
    for j = 7:11
        im = imread(fullfile(file1,files(m).name));
        exp_images(:,j,i)= reshape(im,[],1);
        m = m+1;
    end 
end


sub_images = zeros(243*320,15);


for i = 1:15
      X = exp_images(:,[1:11],i);
      
      X_norm = normalize(X);
      covX = cov(X_norm);
      [V L] = eig(covX);
      l = diag(L);
      per_var = (sum(l(11))/sum(l))*100
      sub_images(:,i) = X_norm*V(:,11);
    
end  

count = 0;
for i = 1:15
    for j = 1:11
        matchM = exp_images(:,j,i);
        matchM = normalize(matchM);
        dist = zeros(1,15);
        
        for k = 1:15
            dist(1,k) = norm(sub_images(:,k) - matchM);
            [mi I] = min(dist);
        end
            if I == i
               count = count+1;
              
            end
    end

end

count
