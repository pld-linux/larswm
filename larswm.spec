Summary:	Lars Tiling Window Manager
Summary(pl):	Zarz±dca okien larswm
Name:		larswm
Version:	7.2.10
Release:	1
License:	GPL
Group:		X11/Window Managers
Source0:	http://www.fnurt.net/larswm/%{name}-%{version}.tar.gz
# Source0-md5:	a97f4287386d3cef3fd8675a0dcf7b38
Source1:        %{name}-xsession.desktop
URL:		http://www.fnurt.net/larswm/
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tiling window manager for X, based on David Hogan's 9wm. It provides
virtual desktops, support for tiled and untiled windows, keyboard
shortcuts and more, while using very little system resources. Please
see http://www.fnurt.net/larswm/ for more information.

%description -l pl
Zarz±dca okien dla X oparty na 9wm. Umo¿liwia korzystanie z
wirtualnych desktopów, okienek "tiled" i "untiled", skrótów
klawiszowych i wiele wiêcej przy niewielkim zapotrzebowaniu na zasoby
systemowe. Wiêcej informacji znajduje siê pod adresem
http://www.fnurt.net/larswm/ .

%prep
%setup -q

%build
xmkmf -a
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install install.man \
	BINDIR=%{_bindir} \
	MANDIR=%{_mandir}/man1 \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/xsessions
install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/xsessions/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README README.9wm ChangeLog sample.* *.ms
%attr(0755,root,root) %{_bindir}/*
%{_datadir}/xsessions/%{name}.desktop
%{_mandir}/man1/*
