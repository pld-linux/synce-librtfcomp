Summary:	SynCE - Compressed RTF extensions
Name:		synce-librtfcomp
Version:	1.1
Release:	0.1
License:	MIT
Group:		Libraries
Source0:	http://dl.sourceforge.net/synce/librtfcomp-%{version}.tar.gz
# Source0-md5:	b7f70dc41687d920ec9f47c01f56d6ce
URL:		http://www.synce.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	python-Pyrex
BuildRequires:	python-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%package devel
Summary:	Header files for librtfcomp library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel

%prep
%setup -q -n librtfcomp-%{version}
# XXX - fix the test
sed -i -e s/have_gccvisibility=yes/have_gccvisibility=no/ configure.in

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_bindir}/test{,rtf}
rm -f $RPM_BUILD_ROOT%{py_sitedir}/pyrtfcomp.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fromrtf
%attr(755,root,root) %{_bindir}/testrtf
%attr(755,root,root) %{_bindir}/tortf
%attr(755,root,root) %{_libdir}/librtfcomp.so.*.*.*
%{py_sitedir}/pyrtfcomp.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/rtfcomp
%{_libdir}/librtfcomp.la
