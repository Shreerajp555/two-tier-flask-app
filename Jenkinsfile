@Library("shared") _
pipeline{
    agent {label "dev"}
    stages{
        stage("code clone"){
            steps{
                script{
                    clone("https://github.com/Shreerajp555/two-tier-flask-app.git", branch: "main")
                }
            }
        }
        stage("Trivy File sys Scan"){
            steps{
                sh "trivy fs . -o resutls.json"
            }
        }
        stage("build"){
            steps{
                sh "docker build -t two-tier-flask-app ."
            }
        }
        stage("test"){
            steps{
                echo "testing will doen by test team"
            }
        }
        stage("Push to DockerHub"){
            steps{
                withCredentials([usernamePassword(
                    credentialsId:"dockerHubCreds",
                    passwordVariable:"dockerHubPass",
                    usernameVariable:"dockerHubUser"
                    )]){
                        sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPass}"
                        sh "docker image tag two-tier-flask-app ${env.dockerHubUser}/two-tier-flask-app:latest"
                        sh "docker push ${env.dockerHubUser}/two-tier-flask-app:latest"
                    }
            }
        }
        stage("deploy"){
            steps{
                sh "docker compose up -d --build flaskapp"
            }
        }
    }
    post{
        success{
            emailext(
                subject: "build successful",
                body: "good news  your build was successful",
                to: 'shreerajpatil29@gmail.com'
                )
        }
        failure{
            emailext(
                subject: "build failed",
                body: "Bad news your build was failed",
                to: 'shreerajpatil29@gmail.com'
                )
        }
    }
}
