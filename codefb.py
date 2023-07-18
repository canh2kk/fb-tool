
<!DOCTYPE html>
<html>
<head>
    <title>Facebook Login</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f3f3f3;
        }
        
        #container {
            width: 400px;
            margin: 100px auto;
            background-color: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 5px rgba(0, 0, 0, 0.3);
        }
        
        h2 {
            text-align: center;
            color: #3b5998;
        }
        
        .form-group {
            margin-bottom: 20px;
        }
        
        .form-group label {
            display: block;
            margin-bottom: 5px;
            color: #888;
        }
        
        .form-group input[type="text"],
        .form-group input[type="password"] {
            width: 100%;
            height: 30px;
            padding: 5px;
            border-radius: 3px;
            border: 1px solid #ddd;
        }
        
        .form-group button {
            width: 100%;
            height: 40px;
            background-color: #3b5998;
            color: #fff;
            font-size: 16px;
            border: none;
            border-radius: 3px;
            cursor: pointer;
        }
        
        .form-group button:hover {
            background-color: #2a437f;
        }
    </style>
</head>
<body>
    <div id="container">
        <h2>Log in to Facebook</h2>
        <form>
            <div class="form-group">
                <label for="email">Email or Phone</label>
                <input type="text" id="email" required>
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" id="password" required>
            </div>
            <div class="form-group">
                <button type="submit">Log In</button>
            </div>
        </form>
    </div>
</body>
</html>

