# Unichunks Documentation

## Time Series Models Documentation

### ARIMA (Autoregressive Integrated Moving Average)
**Category**: Statistical Time Series Model
**Description**: ARIMA is a classical statistical method for time series forecasting that combines autoregression, differencing, and moving average components.

**Key Components**:
- AR (Autoregression): Uses past values to predict future values
- I (Integration/Differencing): Makes the time series stationary
- MA (Moving Average): Uses past forecast errors in the prediction

**Implementation References**:
- Box, G. E., Jenkins, G. M., Reinsel, G. C., & Ljung, G. M. (2015). Time series analysis: forecasting and control.

---

### SARIMA (Seasonal ARIMA)
**Category**: Statistical Time Series Model
**Description**: SARIMA extends ARIMA by incorporating seasonal components, making it particularly useful for time series data with recurring patterns.

**Key Components**:
- Regular ARIMA components (p,d,q)
- Seasonal components (P,D,Q,s)
- Handles both trend and seasonal patterns

**Implementation References**:
- Box, G. E., Jenkins, G. M., Reinsel, G. C., & Ljung, G. M. (2015). Time series analysis: forecasting and control.

---

### GARCH (Generalized Autoregressive Conditional Heteroskedasticity)
**Category**: Volatility Time Series Model
**Description**: GARCH models are specifically designed for modeling time-varying volatility in time series data.

**Key Components**:
- Conditional variance modeling
- Volatility clustering
- Risk assessment capabilities

**Implementation References**:
- Bollerslev, T. (1986). Generalized autoregressive conditional heteroskedasticity.

---

### XGBoost
**Category**: Machine Learning Model
**Description**: XGBoost is a gradient boosting framework that can be applied to time series forecasting through feature engineering.

**Key Components**:
- Gradient boosting
- Tree-based learning algorithms
- Advanced regularization

**Implementation References**:
- Chen, T., & Guestrin, C. (2016). XGBoost: A Scalable Tree Boosting System.

---

## Model Comparison Section
The performance comparison of these models can be found in the referenced accuracy table. Each model brings different strengths to time series analysis:

1. ARIMA: Best for linear time series with clear trend patterns
2. SARIMA: Optimal for seasonal data with recurring patterns
3. GARCH: Specialized for volatility forecasting
4. XGBoost: Excellent for complex, non-linear relationships in time series data

For detailed performance metrics, refer to the maximum accuracy table in the original research.