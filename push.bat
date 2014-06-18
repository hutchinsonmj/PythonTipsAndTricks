set /p message="Enter commit message: 
" %=%
call git add --all
call git commit -m "%message%"
call git push
