# Metro-X

This is a solution to GeekTrust backend design problem : [Metro Card](https://www.geektrust.com/coding/detailed/metro-card)

## Setup Instructions

### 1. Create a Virtual Environment

**Windows:**
```
python -m venv venv
```

**Linux/Mac:**
```
python3 -m venv venv
```

### 2. Activate the Virtual Environment

**Windows:**
```
venv\Scripts\activate
```

**Linux/Mac:**
```
source venv/bin/activate
```

### 3. Install Requirements

```
pip install -r requirements.txt
```

### 4. Run the Main File

```
python main.py sample_input/input1.txt
```

## TODO :
- Add test cases for current development
- Add Support for multiple stations & destinations.
- Add Persistent data-store
- Fare calculation logic needs to be dynamic.
- Containerization
