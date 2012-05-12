Fiber
=====

Fiber aims to be be the easiest way to launch and configure servers on AWS EC2.
The goal is to be much more focused and simpler than full configuration
management solutions. 

Fiber leverages [Fabric](http://docs.fabfile.org/en/1.4.2/index.html) for
command execution and draws several design cueues from this great package.

***Warning:*** *This is a proof of concept - most likely not ready to use, and
definitely subject to major refactoring. If you like the concept, I'd love to
hear about it, get feedback, and even better, help.*

## What it <del>does</del> will do

- Launch servers on EC2 
- Configuring and install server packages

## Example  

    import ConfigParser
    from fiber.api import env, launch

    # Read config
    config = ConfigParser.ConfigParser()
    config.read('config.ini')

    # Fab & server setup
    env.use_ssh_config = True
    env.forward_agent = True
    env.key_filename = config.get('ec2', 'key_filename')
    env.user = config.get('ec2', 'user');
    env.host_webserver_user = config.get('ec2', 'webserver_user')
    env.port = config.get('ec2', 'port')

    server = launch()

## License

Copyright (c) 2012, OMBU Inc. http://ombuweb.com
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

- Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

- Redistributions in binary form must reproduce the above copyright notice, this
  list of conditions and the following disclaimer in the documentation and/or
  other materials provided with the distribution.

- Neither the name of OMBU INC. nor the names of its contributors may be used to
  endorse or promote products derived from this software without specific prior
  written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL OMBU INC. BE LIABLE FOR ANY DIRECT,
INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

