Summary:	kmud - KDE mud client
Summary(pl):	kmud - klient muda dla KDE
Name:		kmud2
Version:	snapshot
Release:	0.1
License:	GPL
Group:		X11/Applications/Games
Source0:	ftp://ftp.kmud.de/pub/kmud/%{name}-%{version}.tar.gz
# Source0-md5:	11274fdd0a6685ef7df4449610131019
Source1:	ftp://ftp.kmud.de/pub/kmud/kde3-admin.tar.gz
# Source1-md5:	13ede60fe87178ec08864e32431eda9e
Patch0:		%{name}-automake-fix.patch
Patch1:		%{name}-makefile-fix.patch
Patch2:		%{name}-const.patch
Patch3:		%{name}-docbook_entity_package.patch
URL:		http://www.kmud.de/
BuildRequires:	artsc-devel
BuildRequires:	kdelibs-devel
BuildRequires:	libjpeg-devel
BuildRequires:	pcre-devel
BuildRequires:	qt-devel >= 3.0.3
BuildRequires:	xrender-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kmud is a graphical MUD client for Linux and other Unix platforms
running KDE. It is a useful and easy-to-use program for all people
that want a nice graphical interface instead of a simple telnet for
playing MUDs. It features a connection wizard/profiles, an automapper,
aliases, triggers (also color triggers, regex support), an input
history (with intelligent browsing), a split screen in the view
history scrollback, numpad walking, speed walking, ANSI/vt100 support
with color customizing, alternative input line and multiline input, a
logging facility, auto login/auto reconnect, a programmable toolbar,
MCCP (mud client compression protocol) support, and a plugin
interface.

%description -l pl
Kmud jest graficznym klientem mudowym dla Linuksa i innych platform
uniksowych u¿ywaj±cych KDE. Jest to prosty i ³atwy w obs³udze program
dla wszystkich ludzi, którzy chc± posiadaæ ³adny, graficzny interfejs
zamiast prostego telneta do grania w mudy. Program ten posiada
'czarodziei' automatycznej i prostej konfiguracji po³±czeñ oraz
profili. Do tego: automapper, aliasy, triggery (tak¿e kolorowe - do
pod¶wietlania tekstów), historiê komend (wraz z inteligentn±
przegl±dark±), dzielenie ekranu w oknie przegl±dania historii,
chodzenie przy pomocy klawiatury numerycznej, szybkie chodzenie,
wsparcie dla ANSI/vt100 z obs³uga ustawieñ kolorów, alternatywn± liniê
wpisywania komend oraz wieloliniowe wpisywanie, logowanie,
auto-login/reconnect, programowalny pasek przycisków, MCCP oraz
interfejs wtyczek.

%package devel
Summary:	kmud - development files
Summary(pl):	Pliki programistyczne dla kmuda
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
kmud development files.

%description devel -l pl
Pliki programistyczne dla kmuda.

%prep
%setup -q -n kmud2
rm -rf admin
tar xfz %{SOURCE1}
%patch0 -p0
%patch1 -p0
%patch2 -p1
%patch3 -p1

%build
%{__make} -f Makefile.dist
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

# TODO: add Categories (if not present already)
install -d $RPM_BUILD_ROOT%{_desktopdir}
mv -f $RPM_BUILD_ROOT{%{_datadir}/applnk/Games/*.desktop,%{_desktopdir}}

%find_lang kmud --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f kmud.lang
%defattr(644,root,root,755)
%doc README ChangeLog TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libkmud.so.*.*.*
%attr(755,root,root) %{_libdir}/kde3/*.so
%{_libdir}/kde3/*.la
%{_datadir}/apps/*
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/kmud
%{_datadir}/services/*
%{_datadir}/servicetypes/*
%{_desktopdir}/*.desktop

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkmud.so
%{_libdir}/libkmud.la
%{_includedir}/kmud
