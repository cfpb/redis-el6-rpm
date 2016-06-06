# REDIS-3.0.7 RPM built for RHEL 6.X

**Description**:  
Redis is a key-value database. It is similar to memcached but the dataset is not volatile, and values can be strings, exactly like in memcached, but also
lists and sets with atomic operations to push/pop elements.

In order to be very fast but at the same time persistent the whole dataset is taken in memory and from time to time and/or when a number of changes to the
dataset are performed it is written asynchronously on disk. You may lose the last few queries that is acceptable in many applications but it is as fast
as an in memory DB (beta 6 of Redis includes initial support for master-slave replication in order to solve this problem by redundancy).

Compression and other interesting features are a work in progress. Redis is written in ANSI C and works in most POSIX systems like Linux, *BSD, Mac OS X,
and so on. Redis is free software released under the very liberal BSD license.


  - **Technology stack**: 

    Redis is an open source, BSD licensed, advanced key-value cache and store. It is often referred to as a data structure server since keys can contain strings, hashes, lists, sets, sorted sets, bitmaps and hyperloglogs.

=======

## Dependencies

The build process for the redis rpm requires the devel (x86_64) packages. 
And this redis package is intended for an x86_64 system.

## Installation

Build RPM using Vagrant

1. The repo is cloned into a local sandbox
2. Run "vagrant up" to build the VM.
3. Run "vagrant ssh" to connect to VM.
4. Run "rpmbuild -ba SPECS/redis.spec" to build the redis rpm package.

Build RPM on server

1. Once repo is cloned, run "sh ./bootstrap.sh"
2. cd to ~/rpmbuild 
3. Run "rpmbuild -ba /SPECS/redis.spec"

Installing the RPM 

Install the built RPM by running "sudo yum install RPMS/x86_64/redis-3.0.7-1.el6.x86_64.rpm"

## Configuration

    Edit the SPEC file ($HOME/rpmbuild/SPEC/redis.spec) to make necessary changes to the build configuration

=======


## Known issues

    There are no known issues related to this build process.
    It is required to have the tclsh package installed 

## Getting help

If you have questions, concerns, bug reports, etc, please file an issue in this repository's Issue Tracker.


## Getting involved

For general instructions on _how_ to contribute, please refer to [CONTRIBUTING](CONTRIBUTING.md).


----

## Open source licensing info
1. [TERMS](TERMS.md)
2. [LICENSE](LICENSE)
3. [CFPB Source Code Policy](https://github.com/cfpb/source-code-policy/)


----

## Credits and references

See below links for more information and community support.

    http://redis.io/community
    
