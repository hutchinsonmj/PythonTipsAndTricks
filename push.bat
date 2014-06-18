set /p message="Enter commit message\n" %=%
call git add --all
call git commit -m "%message%"
call git push