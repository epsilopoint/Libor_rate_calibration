# Libor_rate_calibration
Calibration of Libor rates with Vasicek model

I use the Vasicek model to generate Stochastic modelling with the following stochastic equation

$$ dr_t= a(b-r_t)d_t+\sigma dW_t $$

where $b$ is long term mean value, $a$ speed of reversion and $\sigma$ instantaneous volatility. 

We will be use methods proposed by Thijs van den Berg in Calibrating the Ornstein-Uhlenbeck(Vasicek) model to 
estimate $a,b,\sigma$ and having this, generate stochastic process. 

I annalyesd data of 12 month Libor rates for period 01-01-2000 -- 01-12-2021 used from http://www.fedprimerate.com/libor/libor_rates_history.htm#:~:text=LIBOR%20rates%20are%20fixed%20every%20UK%20business%20day,which%20participate%20in%20the%20London%20wholesale%20money%20market.
