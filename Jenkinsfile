pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building Shopping Application...'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m pytest test_app.py -v'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Shopping Application...'
            }
        }
    }
}
