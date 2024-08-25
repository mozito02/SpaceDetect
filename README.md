
# SpaceDetect

SpaceDetect is a Django web application that leverages a Random Forest model to predict the hazard level of Near-Earth Objects (NEOs). The app provides a user-friendly interface to input NEO characteristics and receive a prediction on whether the object is hazardous.

## Features

- **Prediction Form**: A form for users to input NEO data.
- **Model Integration**: Utilizes a pre-trained Random Forest model to determine the hazard level of the NEO.

## Technologies Used

- **Django**: A high-level Python web framework for rapid development.
- **Django REST Framework**: Provides a powerful toolkit for building APIs.
- **Bootstrap 5**: For responsive and modern design.
- **Pickle**: For loading and using the pre-trained machine learning model.
- **NumPy**: Used for numerical operations and data handling.


## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/mozito02/SpaceDetect.git
   cd SpaceDetect
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Add your model file** (`SpaceDetect` or your specific model file) to the project directory.

5. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

6. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

7. **Access the application:**

   Open your browser and go to `http://127.0.0.1:8000/predict` to view the application.

## Usage

1. **Input NEO characteristics** into the form:
   - **Estimated Diameter Min**
   - **Estimated Diameter Max**
   - **Relative Velocity**
   - **Miss Distance**
   - **Absolute Magnitude**

2. **Click "Predict"** to get the result indicating whether the NEO is hazardous.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the application.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
