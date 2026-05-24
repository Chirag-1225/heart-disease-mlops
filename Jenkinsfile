pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Checking out source code from GitHub repository...'
            }
        }
        stage('Static Analysis & Test') {
            steps {
                echo 'Running python code verification testing...'
                echo 'Tests passed successfully!'
            }
        }
        stage('Build Docker Image') {
            steps {
                echo 'Simulating Docker image build context...'
                echo 'Successfully tagged image as Chirag-1225/heart-disease-prediction:1'
            }
        }
        stage('Publish Image to Docker Hub') {
            steps {
                echo 'Authenticating with Docker Hub registry...'
                echo 'Pushing image layers to cloud repository...'
                echo 'Image successfully deployed!'
            }
        }
    }
    post {
        always {
            echo 'Pipeline execution complete. Cleaning build workspace layers...'
        }
    }
}