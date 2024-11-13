*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  juho
    Set Password  juho1919
    Set Password Confirmation  juho1919
    Submit Credentials  Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ju
    Set Password  juho1919
    Set Password Confirmation  juho1919
    Submit Credentials  Register
    Register Should Fail With Message  Username must be at least 3 characters long and contain only lowercase letters (a-z)

Register With Valid Username And Too Short Password
    Set Username  juho
    Set Password  ju1
    Set Password Confirmation  ju1
    Submit Credentials  Register
    Register Should Fail With Message  Password must be at least 8 characters long


Register With Valid Username And Invalid Password
    Set Username  juho
    Set Password  juhooooooo
    Set Password Confirmation  juhooooooo
    Submit Credentials  Register
    Register Should Fail With Message  Password must contain at least one non-letter character

Register With Nonmatching Password And Password Confirmation
    Set Username  juho
    Set Password  juho1919
    Set Password Confirmation  juho191
    Submit Credentials  Register
    Register Should Fail With Message  Password and Password confirmation don't match

Register With Username That Is Already In Use
    Set Username  juhotest
    Set Password  juhotest1919
    Set Password Confirmation  juhotest1919
    Submit Credentials  Register
    Register Should Fail With Message  Username is already taken

Login After Successful Registration
    Set Username  juho
    Set Password  juho1919
    Set Password Confirmation  juho1919
    Submit Credentials  Register
    Click Link  Continue to main page
    Click Button  Logout
    Set Username  juho
    Set Password  juho1919
    Submit Credentials  Login
    Login Should Succeed

Login After Failed Registration
    Set Username  ju
    Set Password  juho1919
    Set Password Confirmation  juho1919
    Submit Credentials  Register
    Register Should Fail With Message  Username must be at least 3 characters long and contain only lowercase letters (a-z)
    Click Link  Login
    Set Username  ju
    Set Password  juho1919
    Submit Credentials  Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Register Should Succeed
    Welcome Page Should Be Open

Logout Should Succeed
    Login Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    [Arguments]  ${button_name}
    Click Button  ${button_name}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  juhotest  juhotest1919
    Go To Register Page