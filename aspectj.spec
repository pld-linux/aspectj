Summary:	A seamless aspect-oriented extension to the Java programming language
Summary(pl.UTF-8):	Przezroczyste zorientowane aspektowo rozszerzenie dla języka Java
Name:		aspectj
Version:	1.6.0
Release:	1
License:	CPL v1.0
Group:		Development/Languages
Source0:	http://download.eclipse.org/tools/aspectj/%{name}-%{version}.jar
# Source0-md5:	6648c5c594638a67c08a40585396b2f3
URL:		http://eclipse.org/aspectj/
Requires:	jre >= 1.4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	%{_libdir}/java
%define		_javadatadir	%{_datadir}/java

%description
A seamless aspect-oriented extension to the Java programming language.

%description -l pl.UTF-8
Przezroczyste zorientowane aspektowo rozszerzenie dla języka Java.

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_javadatadir},%{_bindir}}

install lib/*.jar $RPM_BUILD_ROOT%{_javadatadir}

cat <<EOF >$RPM_BUILD_ROOT%{_bindir}/ajbrowser
#!/bin/sh

[ -z "\$JAVA_HOME" ] && JAVA_HOME=%{_javalibdir}
[ -z "\$ASPECTJ_HOME" ] && ASPECTJ_HOME=%{_javadatadir}

java -classpath "\$ASPECTJ_HOME/aspectjtools.jar:\$JAVA_HOME/lib/tools.jar:\$CLASSPATH" -Xmx64M org.aspectj.tools.ajbrowser.Main "\$@"
EOF

cat <<EOF >$RPM_BUILD_ROOT%{_bindir}/ajc
#!/bin/sh

[ -z "\$JAVA_HOME" ] && JAVA_HOME=%{_javalibdir}
[ -z "\$ASPECTJ_HOME" ] && ASPECTJ_HOME=%{_javadatadir}

java -classpath "\$ASPECTJ_HOME/aspectjtools.jar:\$JAVA_HOME/lib/tools.jar:\$CLASSPATH" -Xmx64M org.aspectj.tools.ajc.Main "\$@"
EOF

cat <<EOF >$RPM_BUILD_ROOT%{_bindir}/ajdoc
#!/bin/sh

[ -z "\$JAVA_HOME" ] && JAVA_HOME=%{_javalibdir}
[ -z "\$ASPECTJ_HOME" ] && ASPECTJ_HOME=%{_javadatadir}

java -classpath "\$ASPECTJ_HOME/aspectjtools.jar:\$JAVA_HOME/lib/tools.jar:\$CLASSPATH" -Xmx64M org.aspectj.tools.ajdoc.Main "\$@"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat <<EOF

 Rmember to add %{_javadatadir}/aspectjtools.jar to your CLASSPATH.
 This small .jar file contains classes required by any program
 compiled with the ajc compiler.

EOF

%files
%defattr(644,root,root,755)
%doc README* LICENSE* doc/*
%attr(755,root,root) %{_bindir}/*
%{_javadatadir}/*.jar
