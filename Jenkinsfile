pipeline {
    agent any 

    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
        stage('Run Python Tests') {
            steps {
                // Checkout the code from the repo
                git 'https://github.com/SelvaraniDG/Calculator.git'
                
                // // Run unit tests
                // sh 'python -m unittest test_calculator.py'
            }
        }
    }
}
