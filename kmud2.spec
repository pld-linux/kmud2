Summary:	kmud - KDE mud client
Summary(pl):	kmud - mud client dla KDE
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
URL:		http://www.kmud.de
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
Kmud jest graficznym klientem mudowym dla Linuksa i innych paltfrom
Uniksowych u¿ywaj±cych KDE. Jest to prosty i ³atwy w obs³udze program
dla wszystkich ludzi, którzy chc± posiadaæ ³adny, graficzny interfejs
zamiast prostego telneta do grania w mudy. Program ten posiada
'czarodziei' automatycznej i prostej konfiguracji po³±czeñ oraz
profili. Do tego: automapper, aliasy, triggery (tak¿e kolorowe - do
pod¶wietlania tekstów), historiê komend (wraz z inteligetn±
przegl±dark±), dzielenie ekranu w oknie przegl±dania historii,
chodzenie przy pomocy klawiatury numerycznej, szybkie chodzenie,
wsparcie dla ANSII/vt100 z obs³uga ustawieñ kolorów, alternatywn±
liniê wpisywania komend oraz wieloliniowe wpisywanie, logowanie,
auto-login/reconnect, programowalny pasek przycisków, MCCP oraz
interfejs wtyczek.


%prep

%setup -q -n kmud2
rm -rf admin
tar xfz %{SOURCE1}
%patch0 -p0
%patch1 -p0

%build

%{__make} -f Makefile.dist
%configure
%{__make}


%install
#rm -rf $RPM_BUILD_ROOT
#%{__make} install \
#	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT
%clean
#rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%doc README FAQ ChangeLog TODO
%attr(755,root,root) %{_bindir}/*
