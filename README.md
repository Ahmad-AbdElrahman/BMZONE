
# Construction Material Procurement Web Application

## Overview

The construction industry in Egypt faces significant cost overruns due to inefficient material procurement processes for ready-mix concrete plants and contractors. Sourcing and comparing materials that meet specific project requirements is time-consuming and lacks transparency. This often leads to suboptimal material selection, resulting in cost increases and potentially compromised project quality. Existing solutions in the market primarily focus on material databases and pricing information, neglecting the technical aspects of material selection.

Our proposed application bridges this gap by providing a user-friendly platform with a comprehensive database of materials, detailed specifications, pricing information, and advanced search filters tailored to local project needs. Additionally, the application offers a unique consultancy feature that recommends suitable materials based on project requirements (e.g., strength, durability). Users can further connect with qualified professionals through the platform for in-depth consultations. This will empower users to make informed decisions based on project needs, optimize costs, and streamline communication with suppliers. By focusing on user-friendliness, data accuracy, and integration with local suppliers, our application aims to revolutionize the material procurement process and improve project quality in the Egyptian construction industry.

## Features

- **Comprehensive Material Database**: Access a wide range of construction materials with detailed specifications and pricing information.
- **User-Friendly Interface**: Easy-to-use platform designed to enhance the user experience.
- **Local Supplier Integration**: Seamless integration with local suppliers for accurate and up-to-date information.

## Technology Stack

- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript
- **Database**: sqlite

## Installation

### Prerequisites

- Python 3.8+

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/construction-material-procurement.git
   cd construction-material-procurement
   ```

2. **Build and Run the Application Using Docker**
   ```bash
   python manage.py runserver
   ```

3. **Apply Migrations**
   ```bash
    python manage.py migrate
   ```

4. **Create a Superuser**
   ```bash
   python manage.py createsuperuser
   ```

5. **Access the Application**
   Open your browser and navigate to `http://localhost:8000`.

## Usage

1. **Register and Login**: Users can register and log in to the platform to access all features.
2. **Search for Materials**: Use advanced filters to search for materials that meet your project requirements.

## Contribution

We welcome contributions to improve the platform. Please follow these steps to contribute:

1. **Fork the Repository**
2. **Create a Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Commit Your Changes**
   ```bash
   git commit -m 'Add some feature'
   ```
4. **Push to the Branch**
   ```bash
   git push origin feature/your-feature-name
   ```
5. **Open a Pull Request**

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any inquiries or support, please contact us at support@construction-material-procurement.com.
