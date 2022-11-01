# Libor_rate_calibration
Calibration of Libor rates with Vasicek model

I use the Vasicek model to generate Stochastic modelling with the following stochastic equation

$$ dr_t= a(b-r_t)d_t+\sigma dW_t $$

where $b$ is long term mean value, $a$ speed of reversion and $\sigma$ instantaneous volatility. 

We will be use methods proposed by Thijs van den Berg in Calibrating the Ornstein-Uhlenbeck(Vasicek) model to 
estimate $a,b,\sigma$ and having this, generate stochastic process. 
