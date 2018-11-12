
# data
X <- as.numeric(readLines("sample20.txt"))

# descriptive
mean(X)
median(X)

var(X)
range(X)

hist(X)

## frequentist
mean(X)

## likelihood

# statistical model N(theta,known var=25)

x <- seq(-5,5,0.01)

plot(x,y=dnorm(x,0,1))

sum(dnorm(x[1:500],0,1))/sum(dnorm(x,0,1))

plot(x,y=pnorm(x,0,1))

# plot(seq(0,1,0.01), qnorm(seq(0,1,0.01),0,1))

# p(D|theta=170)

pnorm(160,mean=170,sd=5)  
pnorm(170,mean=170,sd=5)
pnorm(180,mean=170,sd=5)

dnorm(160,mean=170,sd=5)
dnorm(170,mean=170,sd=5)
dnorm(180,mean=170,sd=5)

# but we are interested in the inverse problem

dnorm(175.1,mean=160,sd=5)
dnorm(175.1,mean=170,sd=5)
dnorm(175.1,mean=180,sd=5)

# for any observed data, we consider P(X|theta) as a function of theta

thetas <- seq(160, 190, 0.01)

prod(dnorm(X,thetas[1],5))

L <- c()
for (theta in thetas) L <- c(L, prod(dnorm(theta,X,5)))

plot(x=thetas, y=L, xlab="theta", ylab="likelihood")

# numerical solution

# 1 - grid search
thetas[which.max(L)]

# 2 - random search

# 3 - algorithm

# analytical solution


# more data

X <- as.numeric(readLines("sample1000.txt"))
mean(X)
thetas <- seq(160, 190, 0.01)

L <- c()
for (theta in thetas) L <- c(L, prod(dnorm(theta,X,5)))

thetas[which.max(L)]

logL <- c()
for (theta in thetas) logL <- c(logL, sum(dnorm(theta,X,5,log=TRUE)))

thetas[which.max(logL)]

## hypothesis testing

# LRT

X <- as.numeric(readLines("sample20.txt"))

thetas <- seq(160, 190, 0.01)

logL <- c()
for (theta in thetas) logL <- c(logL, sum(dnorm(theta,X,5,log=TRUE)))

thetas[which.max(logL)]

1-pchisq(2*(max(logL)-logL[which(thetas==170)]),df=1)

1-pchisq(2*(max(logL)-logL[which(thetas==174)]),df=1)

1-pchisq(2*(max(logL)-logL[which(thetas==175)]),df=1)


X <- as.numeric(readLines("sample1000.txt"))

thetas <- seq(160, 190, 0.01)

logL <- c()
for (theta in thetas) logL <- c(logL, sum(dnorm(theta,X,5,log=TRUE)))

thetas[which.max(logL)]

1-pchisq(2*(max(logL)-logL[which(thetas==170)]),df=1)

1-pchisq(2*(max(logL)-logL[which(thetas==174)]),df=1)

1-pchisq(2*(max(logL)-logL[which(thetas==175)]),df=1)

# bootstrapping

X <- as.numeric(readLines("sample1000.txt"))

thetas <- seq(160, 190, 0.01)

logL <- c()
for (theta in thetas) logL <- c(logL, sum(dnorm(theta,X,5,log=TRUE)))

theta_mle <- thetas[which.max(logL)]


theta_boot <-c()

for (i in 1:100) {

	Xs <- sample(X, replace=T)

	logL <- c()
	for (theta in thetas) logL <- c(logL, sum(dnorm(theta,Xs,5,log=TRUE)))

	theta_boot[i] <- thetas[which.max(logL)]

	print(theta_boot[i])

}

hist(theta_boot)
abline(v=theta_mle, lty=2)

quantile(theta_boot, c(0.025,0.975))




