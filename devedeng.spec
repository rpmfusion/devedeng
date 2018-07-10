%global commit f0893b3ff7b14723bd148db35bdfe2d284156d19

Name:           devedeng
Version:        4.12.0
Release:        2%{?dist}
Summary:        A program to create video DVDs and CDs (VCD, sVCD or CVD)

License:        GPLv3+
URL:            http://www.rastersoft.com/programas/devede.html
Source0:        https://gitlab.com/rastersoft/devedeng/repository/archive.tar.gz?ref=%{version}#/%{name}-%{version}.tar.gz
Source1:        devede_ng.py.appdata.xml

BuildArch:      noarch

Provides:       devede = %{version}-%{release}
Obsoletes:      devede < 4.0

BuildRequires:  python3-devel
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
#Requires:       mplayer
#Requires:       mpv
Requires:       vlc
Requires:       ffmpeg
Requires:       dvdauthor
Requires:       vcdimager
#Requires:       genisoimage
Requires:       mkisofs
Requires:       brasero
#Requires:       k3b
Requires:       ImageMagick
Requires:       python3-urllib3 
Requires:       python3-gobject
Requires:       python3-cairo
Requires:       python3-dbus
Requires:       dejavu-sans-fonts
Requires:       hicolor-icon-theme


%description
DevedeNG is a program to create video DVDs and CDs (VCD, sVCD or CVD), 
suitable for home players, from any number of video files, in any of the 
formats supported by FFMpeg.  

The suffix NG is because it is a rewrite from scratch of the old Devede, to 
work with Python3 and Gtk3, and with a new internal architecture that allows 
to expand it and easily add new features.


%prep
%autosetup -n %{name}-%{version}-%{commit}


%build
%py3_build

# Remove shebang from Python libraries
for lib in build/lib/devedeng/*.py; do
  sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
  touch -r $lib $lib.new &&
  mv $lib.new $lib
done


%install
%py3_install 

# Fix desktop file 
desktop-file-install \
  --delete-original \
  --add-category X-OutputGeneration \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/devede_ng.py.desktop

# Remove icon
rm %{buildroot}%{_datadir}/pixmaps/%{name}.svg

# Add docs
install -p -m 644 HISTORY.md %{buildroot}%{_pkgdocdir}
install -p -m 644 README.md %{buildroot}%{_pkgdocdir}

# Install AppData file
install -d %{buildroot}%{_datadir}/metainfo
install -p -m 644 %{SOURCE1} %{buildroot}%{_datadir}/metainfo
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml

%find_lang %{name}


%files -f %{name}.lang
%{_bindir}/devede_ng.py
%{_bindir}/copy_files_verbose.py
%{_datadir}/%{name}
%{python3_sitelib}/%{name}*.egg-info
%{python3_sitelib}/%{name}
%{_datadir}/metainfo/devede_ng.py.appdata.xml
%{_datadir}/applications/devede_ng.py.desktop
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%exclude %{_mandir}/man1/devede.1*
%doc %{_docdir}/%{name}
%license COPYING


%changelog
* Tue Jul 10 2018 Miro Hrončok <mhroncok@redhat.com> - 4.12.0-2
- Rebuilt for Python 3.7

* Sat Jun 30 2018 Andrea Musuruane <musuruan@gmail.com> - 4.12.0-1
- Updated to new upstream release
- Upstream git repository moved to gitlab

* Thu May 17 2018 Andrea Musuruane <musuruan@gmail.com> - 4.11.0-2
- Fixed AppData file

* Thu May 03 2018 Andrea Musuruane <musuruan@gmail.com> - 4.11.0-1
- Updated to new upstream release

* Mon Apr 30 2018 Andrea Musuruane <musuruan@gmail.com> - 4.10.0-1
- Updated to new upstream release

* Wed Apr 18 2018 Andrea Musuruane <musuruan@gmail.com> - 4.9.0-1
- Updated to new upstream release

* Thu Jan 25 2018 Andrea Musuruane <musuruan@gmail.com> 4.8.12-1
- Updated to new upstream release
- Removed obsolete scriptlets

* Tue Dec 26 2017 Andrea Musuruane <musuruan@gmail.com> 4.8.11-1
- Updated to new upstream release

* Sat Dec 02 2017 Andrea Musuruane <musuruan@gmail.com> 4.8.10-1
- Updated to new upstream release
- Added AppData file
- Preserved timestamps

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 4.8.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 12 2017 Andrea Musuruane <musuruan@gmail.com> 4.8.9-1
- Updated to new upstream release

* Sun Mar 19 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 4.8.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 08 2017 Andrea Musuruane <musuruan@gmail.com> 4.8.8-1
- Updated to new upstream release

* Thu Feb 02 2017 Andrea Musuruane <musuruan@gmail.com> 4.8.7-1
- Updated to new upstream release

* Sat Dec 17 2016 Andrea Musuruane <musuruan@gmail.com> 4.8.6-1
- Updated to new upstream release

* Sat Nov 26 2016 Andrea Musuruane <musuruan@gmail.com> 4.8.5-1
- Updated to new upstream release

* Sat Nov 05 2016 Andrea Musuruane <musuruan@gmail.com> 4.8.4-1
- Updated to new upstream release

* Sat Oct 29 2016 Andrea Musuruane <musuruan@gmail.com> 4.8.3-1
- Updated to new upstream release

* Sun Sep 25 2016 Andrea Musuruane <musuruan@gmail.com> 4.8.2-1
- Updated to new upstream release

* Tue Sep 06 2016 Andrea Musuruane <musuruan@gmail.com> 4.8.1-1
- Updated to new upstream release

* Sun Aug 14 2016 Andrea Musuruane <musuruan@gmail.com> 4.8.0-1
- Updated to new upstream release

* Thu Aug 04 2016 Andrea Musuruane <musuruan@gmail.com> 4.7.1-1
- Updated to new upstream release

* Mon Apr 25 2016 Andrea Musuruane <musuruan@gmail.com> 4.7.0-1
- Updated to new upstream release

* Thu Mar 17 2016 Andrea Musuruane <musuruan@gmail.com> 4.6.1-1
- First release 

