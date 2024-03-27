pipeline {
    agent {
        docker {
            image 'python:3.12.1-alpine3.19'
            args "-v ${workspace}:/app"
        }
    }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
        stage('Run Python Tests') {
            steps {
                // Checkout the code from the repository
                git 'https://github.com/SelvaraniDG/Calculator.git'
                
                // Run unit tests
                sh 'python -m unittest test_calculator.py'
            }
        }
    }
}
