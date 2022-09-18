# KIRANA CONVERSATION ENGINE
## Who i am?
Hi, i am kirana. My duty is response chat as soon as posible any question from students in the domain of Program Studi Informatika Universitas Amikom Yogyakarta.

They are call me a Chatbot. A smart assistance with AI behind it. Currently i am a stupid baby who need to be trained and impruve rapidly.

I am just only using Python Language. Everyone are welcome for contribute to make me clever everday. There is the milstone.

1st Phase
: Release MVP (Minimum Viable Product) [done]
: Using TFIDF for classify the utterence
: Optimizing TFIDF and store the accuracy

2nd Phase
: Making the engine able to re-train in runtime (without login to remote server)
: Switching the core algorithm in runtime

3nd Phase
: Depending on the result for 1st and 2nd phase

## How to running on your local mechine?
1. Clone the project and enter to the directory
    ```git clone ... ```
2. Create your virtual environment then activate it.
    
    ```
    python3 -m venv ./venv
    source ./venv/bin/activate
    ```
3. Install all dependencies via pip
    ```pip3 install -r requirements.tv```
4. Since kirana has different configuration between local mechine and remote server, we need an ```.env``` files. Create a new file ```.env``` with data below

    ```
    ENV='development'
    ```
5. Lets begin to chit chat with Kirana via console
    ```
    python3 app.py
    ```

---
## Licence
Crafted by hand - Copyright 2022  Arif Akbarul Huda

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE







