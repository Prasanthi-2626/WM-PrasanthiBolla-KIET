# Zone-Aware, Event-Driven Smart Waste Bin Network

**Applicant:** Prasanthi Bolla  
**Institution:** IIITH  
**Repository Name:** WM-PrasanthiBolla-IIITH

---

## Project Overview
Urban waste management is often inefficient due to static collection schedules, overflowing bins, and lack of real-time monitoring.  
This project proposes a **Zone-Aware, Event-Driven Smart Waste Bin Network**, an IoT-based system designed to:

- Monitor bin fill levels in real-time using ultrasonic sensors.
- Trigger alerts only for meaningful events to save energy and bandwidth.
- Aggregate bins into logical zones for smarter decision-making.
- Optimize garbage truck routes dynamically.
- Maintain fail-safe operation during sensor or network failures.

The system is **scalable, reliable, and suitable for real municipal deployments**, with both hardware and software components included.

---

## Repository Structure

WM-PrasanthiBolla-KIET/
│
├── Software/
│ ├── Codes/ # Firmware and software scripts
│ ├── Software_Architecture/ # System flow and MQTT design docs
│ └── Data_Flow/ # Event-driven logic explanation
│
├── Hardware/
│ ├── Codes/ # ESP32 firmware code
│ ├── Hardware_Architecture/ # Bin node, zone gateway, power mgmt
│ └── Components_List/ # Bill of materials
│
├── Diagrams/ # System diagrams and flowcharts
├── README.md # Project overview