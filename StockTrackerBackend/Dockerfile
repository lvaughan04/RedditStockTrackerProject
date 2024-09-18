FROM openjdk:21

ARG JAR_FILE=target/*.jar
COPY ${JAR_FILE} app.jar

EXPOSE 8080

# Command to run the application
ENTRYPOINT ["java","-jar","/app.jar"]

## to build: docker build -t stock-backend:latest .
## to run: docker run -p 8080:8080 stock-backend: latest 
