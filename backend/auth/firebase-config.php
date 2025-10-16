<?php
class FirebaseAuth {
    private $apiKey;
    
    public function __construct($apiKey) {
        $this->apiKey = $apiKey;
    }
    
    // Sign up user
    public function signUp($email, $password, $name) {
        $url = "https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=" . $this->apiKey;
        
        $data = [
            'email' => $email,
            'password' => $password,
            'returnSecureToken' => true
        ];
        
        $response = $this->makeRequest($url, $data);
        
        if (isset($response['localId'])) {
            return [
                'success' => true,
                'uid' => $response['localId'],
                'email' => $email,
                'name' => $name
            ];
        } else {
            return [
                'success' => false,
                'error' => $response['error']['message'] ?? 'Unknown error'
            ];
        }
    }
    
    // Sign in user
    public function signIn($email, $password) {
        $url = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=" . $this->apiKey;
        
        $data = [
            'email' => $email,
            'password' => $password,
            'returnSecureToken' => true
        ];
        
        $response = $this->makeRequest($url, $data);
        
        if (isset($response['localId'])) {
            return [
                'success' => true,
                'uid' => $response['localId'],
                'email' => $email
            ];
        } else {
            return [
                'success' => false,
                'error' => $response['error']['message'] ?? 'Unknown error'
            ];
        }
    }
    
    private function makeRequest($url, $data) {
        $options = [
            'http' => [
                'header' => "Content-Type: application/json\r\n",
                'method' => 'POST',
                'content' => json_encode($data),
                'ignore_errors' => true
            ]
        ];
        
        $context = stream_context_create($options);
        $result = file_get_contents($url, false, $context);
        
        return json_decode($result, true);
    }
}

// Your Firebase API Key
$FIREBASE_API_KEY = "AIzaSyA5-wZiIU9EHreKd460rHccBiPK4I_w2MU";
$firebaseAuth = new FirebaseAuth($FIREBASE_API_KEY);
?>