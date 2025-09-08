```markdown
# Real-Time Network Anomaly Detection System

A real-time anomaly detection system for monitoring network traffic.  
This project captures live packets, processes them through a trained ML model, detects anomalies, and logs alerts.  
It also exposes Prometheus metrics for monitoring.

---

## 🚀 Features
- **Live Traffic Capture** using [Wireshark/tshark](https://www.wireshark.org/).  
- **Anomaly Detection** with ML models (scikit-learn).  
- **Custom Logging** for storing anomalies (`log_module/anomaly_logging.py`).  
- **Alerts** triggered on suspicious activity (`alerts/alert_system.py`).  
- **Prometheus Metrics** (`metrics/prometheus_metrics.py`) for observability.  
- **Web Dashboard** powered by [Streamlit](https://streamlit.io/).  

---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/network-anomaly-detection.git
cd network-anomaly-detection
````

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate  # On Linux/Mac
```

### 3. Install dependencies

```bash
pip install -r requirement.txt
```

---

## ▶️ Usage

### Run the Streamlit dashboard

```bash
streamlit run app.py
```

### Run packet capture + anomaly detection

```bash
python capture/live_capture.py
```

### Start Prometheus (for metrics monitoring)

```bash
prometheus --config.file=prometheus.yml
```

---

## 📊 Output

* **Dashboard:** Displays live anomalies and traffic stats.
* **Logs:** Saved anomalies in `log_module/`.
* **Prometheus:** Exposes metrics at `http://localhost:9090`.

---

## 🛠️ Tech Stack

* **Python**
* **scikit-learn**
* **Streamlit**
* **Wireshark/tshark**
* **Prometheus**

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a new branch (`feature-xyz`)
3. Commit changes
4. Push and open a Pull Request

---

## 📜 License

This project is licensed under the **MIT License** – feel free to use and modify it.

---

