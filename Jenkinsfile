pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', credentialsId: 'jenkins-git', url: 'https://github.com/mohandonga201/chatting-website.git'
            }
        }
        stage('Build Docker Images') {
            steps {
                sh 'docker-compose build'
            }
        }
        stage('Run Tests') {
            steps {
               script {
                    sh '''
                     docker-compose up -d backend
                     docker-compose exec backend sh -c "until nc -z localhost 5000; do sleep 1; done"
                     docker-compose exec backend pytest
            '''
               }
            }
        }
        stage('Deploy Application') {
            steps {
                sh 'docker-compose up -d'
            }
        }
    }
}

