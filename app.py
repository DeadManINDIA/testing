# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.

from flask import Flask
app = Flask('synopsys')

@app.route('/')
def test():
  return "synopsys!\n"

if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 8081)
