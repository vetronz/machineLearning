
# MMFM

thetas <- seq(0,1,0.05)

like <- c()
for (theta in thetas) like <- c(like, (theta^3)*(1-theta)^1)

plot(thetas,like)

thetas[which.max(like)]

tD <- 2*log(max(like)/like[2])

tD

1-pchisq(tD,1)

# prior

belief1 <- 1/thetas
belief1[1] <- NA
belief1 <- belief2/sum(belief2, na.rm=T)

par(mfrow=c(1,3))

plot(thetas,like)
plot(thetas,belief1)
plot(thetas,belief1*like)

belief2 <- 1/thetas^3
belief2[1] <- NA
belief2 <- belief2/sum(belief2, na.rm=T)


pr(mfrow(c(1,3))

plot(thetas,like)
plot(thetas,belief2)
plot(thetas,belief2*like)









