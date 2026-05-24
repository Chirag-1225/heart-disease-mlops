pipeline {
    agent any

    environment {
        DOCKER_REGISTRY_USER = 'your_dockerhub_username' 
        IMAGE_NAME = 'heart-disease-prediction'
        IMAGE_TAG = "${BUILD_NUMBER}"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Chirag-1225/heart-disease-mlops.git'
            }
        }

        stage('Static Analysis & Test') {
            steps {
                echo 'Running python code verification testing...'
                // You can add flake8 or basic unit tests here
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${DOCKER_REGISTRY_USER}/${IMAGE_NAME}:${IMAGE_TAG} ."
                sh "docker tag ${DOCKER_REGISTRY_USER}/${IMAGE_NAME}:${IMAGE_TAG} ${DOCKER_REGISTRY_USER}/${IMAGE_NAME}:latest"
            }
        }

        stage('Publish Image to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', passwordVariable: 'DOCKER_HUB_PASSWORD', usernameVariable: 'DOCKER_HUB_USER')]) {
                    sh "echo \$DOCKER_HUB_PASSWORD | docker login -u \$DOCKER_HUB_USER --password-stdin"
                    sh "docker push ${DOCKER_REGISTRY_USER}/${IMAGE_NAME}:${IMAGE_TAG}"
                    sh "docker push ${DOCKER_REGISTRY_USER}/${IMAGE_NAME}:latest"
                }
            }
        }
    }
    
    post {
        always {
            sh "docker logout"
            echo "Pipeline run completed execution."
        }
    }
}