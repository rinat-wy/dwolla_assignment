output "lambda_function_name" {
  value     = aws_lambda_function.time_function.function_name
  sensitive = true
}
