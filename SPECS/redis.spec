%global _version	3.0.7

Name:			redis	
Version:		%{_version}
Release:		1%{?dist}
Summary:		A persistent key-value database

Group:			Application/Databases
License:		BSD
URL:			http://redis.io
Source0:		http:download.redis.io/releases/redis-3.0.7.tar.gz

Provides:		redis == 3.0.7	

%description
Redis is a key-value database. It is similar to memcached but the dataset is not volatile, and values can be strings, exactly like in memcached, but also
lists and sets with atomic operations to push/pop elements.

In order to be very fast but at the same time persistent the whole dataset is taken in memory and from time to time and/or when a number of changes to the
dataset are performed it is written asynchronously on disk. You may lose the last few queries that is acceptable in many applications but it is as fast
as an in memory DB (beta 6 of Redis includes initial support for master-slave replication in order to solve this problem by redundancy).

Compression and other interesting features are a work in progress. Redis is written in ANSI C and works in most POSIX systems like Linux, *BSD, Mac OS X,
and so on. Redis is free software released under the very liberal BSD license.


BuildRoot: %(mktemp -ud %{_tmppath}/build/%{name}-%{version}-%{release}-XXXXXX)

%prep
%setup -q 


%build
make %{?_smp_mflags}


%install
make install PREFIX=${RPM_BUILD_ROOT}/usr/local 

%files
/usr/local/bin/redis-benchmark
/usr/local/bin/redis-check-aof
/usr/local/bin/redis-check-dump
/usr/local/bin/redis-cli
/usr/local/bin/redis-sentinel
/usr/local/bin/redis-server

%doc



%changelog

