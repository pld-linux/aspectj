Summary:	A seamless aspect-oriented extension to the Java programming language
Name:		aspectj
Version:	1.2
Release:	0.1
License:	CPL v1.0
Group:		Development/Languages
Source0:	http://download.eclipse.org/technology/ajdt/%{name}-%{version}.jar
# Source0-md5:	70b3d558a510d2eb142930bd3d93eeec
URL:		http://eclipse.org/aspectj/
Requires:	jre >= 1.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	%{_datadir}/java

%description

%prep
%setup -qc

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javalibdir}

install lib/*.jar $RPM_BUILD_ROOT%{_javalibdir}

cat <<EOF >$RPM_BUILD_ROOT%{_bindir}/ajbrowser
#!/bin/sh

if [ "$JAVA_HOME" = "" ] ; then JAVA_HOME=/usr/lib/java
fi
if [ "$ASPECTJ_HOME" = "" ] ; then ASPECTJ_HOME=/tmp/aspectj1.2
fi

java -Xmx64M org.aspectj.tools.ajbrowser.Main "$@"
EOF

cat <<EOF >$RPM_BUILD_ROOT%{_bindir}/ajc
#!/bin/sh

if [ "$JAVA_HOME" = "" ] ; then JAVA_HOME=/usr/lib/java
fi
if [ "$ASPECTJ_HOME" = "" ] ; then ASPECTJ_HOME=/tmp/aspectj1.2
fi

java -Xmx64M org.aspectj.tools.ajc.Main "$@"
EOF

cat <<EOF >$RPM_BUILD_ROOT%{_bindir}/ajdoc
#!/bin/sh

if [ "$JAVA_HOME" = "" ] ; then JAVA_HOME=/usr/lib/java
fi
if [ "$ASPECTJ_HOME" = "" ] ; then ASPECTJ_HOME=/tmp/aspectj1.2
fi

java -Xmx64M org.aspectj.tools.ajdoc.Main "$@"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* LICENSE* doc/*
%attr(755,root,root) %{_bindir}/*
%{_javalibdir}/*.jar
