# Odoo Modules Documentation

## Table of Contents
1. [Hospital Management System](#hospital-management-system)
    - [Overview](#overview)
    - [Features](#features)
    - [Installation](#installation)
    - [Usage](#usage)
    - [Screenshots](#screenshots)
    - [Credits](#credits)
2. [Awesome Dashboard](#awesome-dashboard)
    - [Overview](#overview-1)
    - [Features](#features-1)
    - [Installation](#installation-1)
    - [Usage](#usage-1)
    - [Screenshots](#screenshots-1)
    - [Credits](#credits-1)

---

## Hospital Management System

### Overview

The **Hospital Management System (HMS)** module, developed by **Odoomates**, is designed to help hospitals and clinics manage their operations efficiently. It provides tools for managing patients, doctors, appointments, prescriptions, and more.

### Features

- **Patient Management**: Manage patient records, including personal information and medical history.
- **Doctor Management**: Keep track of doctor details and their specializations.
- **Appointments**: Schedule, track, and manage appointments between doctors and patients.
- **Prescriptions**: Create and manage patient prescriptions.
- **Medical History**: Store and retrieve patients' past medical records and diagnoses.
- **Billing and Invoicing**: Generate bills and invoices for patient services.

### Installation

To install the **Hospital Management System**, follow these steps:

1. Clone the module from the repository:

   ```bash
   git clone https://github.com/odoomates/odooapps.git
   ```

2. Place the `hospital` module directory in your Odoo add-ons directory.

3. Update the Odoo app list and install the module:

   ```bash
   ./odoo-bin -u all
   ```

4. Go to the **Apps** menu in Odoo, search for "Hospital Management System," and click **Install**.

### Usage

1. **Patient Management**:
   - Navigate to **Hospital → Patients**.
   - Add new patients or edit existing patient records.

2. **Appointments**:
   - Navigate to **Hospital → Appointments** to schedule or manage appointments.

3. **Doctor Management**:
   - Navigate to **Hospital → Doctors** to manage doctor records and assign appointments.

4. **Prescriptions**:
   - Create new prescriptions for patients under the **Prescriptions** menu.

5. **Billing**:
   - Go to **Hospital → Billing** to manage and generate invoices for patient services.

### Screenshots

![Hospital Dashboard](screenshots/hospital_dashboard.png)

---

### Credits

- **Author**: Odoomates
- **GitHub**: [Odoomates GitHub Repository](https://github.com/odoomates/odooapps)
- **License**: AGPL-3

---

## Awesome Dashboard

### Overview

The **Awesome Dashboard** module, found in the official Odoo documentation, is an example of using the OWL (Odoo Web Library) JavaScript framework to build a dynamic dashboard for Odoo applications. The module demonstrates how to create a customizable dashboard interface with various widgets and data visualizations.

### Features

- **Dynamic Dashboard Layout**: Use the OWL framework to create a flexible layout with customizable dashboard items.
- **Multiple Dashboard Items**: Display data from various Odoo models using custom dashboard components.
- **Configuration Dialog**: Allow users to enable/disable certain dashboard items through a configuration dialog.
- **Use of OWL Components**: Demonstrates the use of OWL components, hooks, and the Odoo registry system.

### Installation

To install the **Awesome Dashboard** module, follow these steps:

1. Clone or download the module files from the [Odoo Official Documentation](https://www.odoo.com/documentation).

2. Place the `awesome_dashboard` module in your Odoo add-ons directory.

3. Update the Odoo app list and install the module:

   ```bash
   ./odoo-bin -u all
   ```

4. Go to the **Apps** menu in Odoo, search for "Awesome Dashboard," and click **Install**.

### Usage

1. **Dashboard Access**:
   - Once installed, navigate to the dashboard via **Dashboard → Awesome Dashboard**.

2. **Adding Dashboard Items**:
   - Use the configuration dialog to enable/disable specific dashboard items.

3. **Customizing the Layout**:
   - The dashboard layout can be customized using the OWL `Layout` component, allowing flexible positioning of the widgets.

4. **Components Used**:
   - The module uses OWL components such as `Layout`, `Dialog`, and `CheckBox`, as well as custom components like `DashboardItem`.

### Screenshots

![Awesome Dashboard](screenshots/awesome_dashboard.png)

---

### Credits

- **Author**: Odoo Documentation Team
- **Website**: [Odoo Official Documentation](https://www.odoo.com/documentation)
- **License**: LGPL-3

---

### Final Notes

Both the **Hospital Management System** and **Awesome Dashboard** are great examples of how Odoo can be extended using both traditional server-side functionality and modern client-side frameworks like OWL. You can refer to each module’s respective documentation for more details on extending, customizing, and using the modules effectively.

---

This README should give users a clear understanding of how to install, use, and customize both the **Hospital Management System** and the **Awesome Dashboard** modules. Let me know if you need more details or specific customization!