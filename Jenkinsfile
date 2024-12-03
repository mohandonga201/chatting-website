pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/mohandonga201/chatting-website.git'
            }
        }
        stage('Build Docker Images') {
            steps {
                sh 'docker-compose build'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'docker-compose up -d backend'
                sh 'docker-compose exec backend pytest'
            }
        }
        stage('Deploy Application') {
            steps {
                sh 'docker-compose up -d'
            }
        }
    }
}

