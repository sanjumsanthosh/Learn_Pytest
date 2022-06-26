import subprocess


def test_script():
    result = subprocess.run(["python", "hello.py"], capture_output=True, text=True)
    assert result.stdout == "Hello world!!\n"
    
