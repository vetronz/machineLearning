
# assume population is Normal(180,5)
# E[X]=180

ran1 <- rnorm(20, 180, 5)

est1 <- mean(ran1)

est2<-min(ran1)+diff(range(ran1))/2

180-est1
180-est2

est1 <- est2 <- c()

for (i in 1:100) {

	ran1 <- rnorm(20, 180, 5)

	est1[i] <- mean(ran1)

	est2[i]<-min(ran1)+diff(range(ran1))/2

}


plot(x=1:100,y=est1,type="p",col="red")
points(x=1:100,y=est2,col="blue")
abline(h=180,lty=2)

mean(est1)-180

mean(est2)-180

(mean(est1)-180)^2

(mean(est2)-180)^2




