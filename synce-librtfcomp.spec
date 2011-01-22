Summary:	SynCE - Compressed RTF extensions
Summary(pl.UTF-8):	SynCE - rozszerzenia do skompresowanego RTF-a
Name:		synce-librtfcomp
Version:	1.1
Release:	1
License:	LGPL v2.1
Group:		Libraries
Source0:	http://downloads.sourceforge.net/synce/librtfcomp-%{version}.tar.gz
# Source0-md5:	b7f70dc41687d920ec9f47c01f56d6ce
URL:		http://www.synce.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.9
BuildRequires:	libtool
BuildRequires:	python-Pyrex
BuildRequires:	python-devel >= 2.2
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SynCE - Compressed RTF extensions.

%description -l pl.UTF-8
SynCE - rozszerzenia do skompresowanego formatu RTF.

%package devel
Summary:	Header files for librtfcomp library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki librtfcomp
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for librtfcomp library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki librtfcomp.

%package static
Summary:	Static librtfcomp library
Summary(pl.UTF-8):	Statyczna biblioteka librtfcomp
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static librtfcomp library.

%description static -l pl.UTF-8
Statyczna biblioteka librtfcomp.

%package -n python-pyrtfcomp
Summary:	Python binding for librtfcomp library
Summary(pl.UTF-8):	Wiązanie Pythona do biblioteki librtfcomp
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
%pyrequires_eq	python-libs

%description -n python-pyrtfcomp
Python binding for librtfcomp library.

%description -n python-pyrtfcomp -l pl.UTF-8
Wiązanie Pythona do biblioteki librtfcomp.

%prep
%setup -q -n librtfcomp-%{version}
# XXX - fix the test
sed -i -e s/have_gccvisibility=yes/have_gccvisibility=no/ configure.in

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_bindir}/test{,rtf}
rm -f $RPM_BUILD_ROOT%{py_sitedir}/pyrtfcomp.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGELOG
%attr(755,root,root) %{_bindir}/fromrtf
%attr(755,root,root) %{_bindir}/testrtf
%attr(755,root,root) %{_bindir}/tortf
%attr(755,root,root) %{_libdir}/librtfcomp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/librtfcomp.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/librtfcomp.so
%{_libdir}/librtfcomp.la
%{_includedir}/rtfcomp

%files static
%defattr(644,root,root,755)
%{_libdir}/librtfcomp.a

%files -n python-pyrtfcomp
%defattr(644,root,root,755)
%{py_sitedir}/pyrtfcomp.so
