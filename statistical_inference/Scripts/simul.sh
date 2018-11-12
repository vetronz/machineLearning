
# Least concern 10k

java -jar ~/Software/msms/lib/msms.jar -N 10000 -ms 100 400 -t 60 -r 60 100000 > Simul/msms..LC.txt

# Vulnerable 5k

java -jar ~/Software/msms/lib/msms.jar -N 5000 -ms 100 400 -t 30 -r 30 100000 > Simul/msms..VU.txt

# Endangered 2k

java -jar ~/Software/msms/lib/msms.jar -N 2000 -ms 100 400 -t 12 -r 12 100000 > Simul/msms..EN.txt

# Critically endangered 1k

java -jar ~/Software/msms/lib/msms.jar -N 1000 -ms 100 400 -t 6 -r 6 100000 > Simul/msms..CR.txt

# Test 1.5k

java -jar ~/Software/msms/lib/msms.jar -N 1500 -ms 100 1 -t 9 -r 9 100000 > Simul/msms..TEST.txt







