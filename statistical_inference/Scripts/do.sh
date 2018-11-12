
mkdir Simul
mkdir Images_resized
mkdir Images

bash simul.sh 

python createImages.py

mv Images_resized/img..TEST..1.bmp .

python processImages.py




