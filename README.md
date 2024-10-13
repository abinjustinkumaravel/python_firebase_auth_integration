# Python Firebase Authentication Integration

Welcome to the **Python Firebase Authentication Integration** project! This guide will help you set up Firebase authentication in your Python application using the `firebase-admin` SDK.

## Prerequisites

Before you begin, make sure you have the following:

1. **Python 3.6 or later**: Download and install from [python.org](https://www.python.org/).
2. **Pip** (Python package manager): Usually comes pre-installed with Python. To check if you have it, run:
   ```bash
   pip --version
   ```

## Firebase Setup

1. **Create a Firebase Project**:

   - Go to the [Firebase Console](https://console.firebase.google.com/) and click on "Add Project."
   - Follow the on-screen instructions to set up your project.

2. **Add a Service Account Key**:
   - In the Firebase Console, go to your project settings.
   - Navigate to the **Service Accounts** tab.
   - Click on **Generate new private key** and download the JSON file.
   - Save this JSON file in your project's root directory (e.g., `firebase-adminsdk.json`).

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/abinjustinkumaravel/python_firebase_auth_integration.git
   ```

2. **Navigate to the project directory**:

   ```bash
   cd python_firebase_auth_integration
   ```

3. **Create a virtual environment (recommended)**:

   ```bash
   python -m venv venv
   source venv/bin/activate   # For Linux/Mac
   venv\Scripts\activate      # For Windows
   ```

4. **Install the Firebase Admin SDK**:
   ```bash
   pip install firebase-admin
   ```

## Configuration

Add the Firebase service account JSON file to your project and load it in your Python code.

1. **Import the Firebase Admin SDK**:

   ```python
   import firebase_admin
   from firebase_admin import credentials, auth

   # Path to your Firebase service account JSON file
   cred = credentials.Certificate('path/to/firebase-adminsdk.json')

   # Initialize the Firebase app
   firebase_admin.initialize_app(cred)
   ```

2. **Verify the Integration**:
   To verify that your Firebase setup is correct, try creating a new user in Firebase Authentication:
   ```python
   user = auth.create_user(
       email='johndoe@example.com',
       email_verified=False,
       password='password123',
       display_name='John Doe',
       disabled=False
   )
   print('Successfully created new user:', user.uid)
   ```

## Usage

- **Creating a User**:

  ```python
  user = auth.create_user(
      email='janedoe@example.com',
      password='newpassword123',
      display_name='Jane Doe'
  )
  print('Successfully created user:', user.uid)
  ```

- **Fetching User Details**:

  ```python
  user = auth.get_user_by_email('janedoe@example.com')
  print('User data:', user)
  ```

- **Updating User Details**:

  ```python
  user = auth.update_user(
      user.uid,
      email='jane.doe@example.com',
      display_name='Jane D.',
      password='updatedpassword456'
  )
  print('Successfully updated user:', user.uid)
  ```

- **Deleting a User**:
  ```python
  auth.delete_user(user.uid)
  print('Successfully deleted user')
  ```

## Troubleshooting

- **Authentication Errors**: Ensure that the path to the service account JSON file is correct and that your Firebase project has the appropriate permissions.
- **Network Issues**: Check your internet connection, as Firebase requires an active internet connection to communicate with its servers.

## Contributing

Feel free to contribute to this project by creating a pull request or opening an issue. We welcome all contributions to help make this integration better!

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

If you have any questions or feedback, please reach out:

- **GitHub**: [abinjustinkumaravel](https://github.com/abinjustinkumaravel)
- **Email**: abinjustinkumaravel@gmail.com

Happy coding!
