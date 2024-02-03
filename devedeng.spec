Name:           devedeng
Version:        4.17.0
Release:        7%{?dist}
Summary:        A program to create video DVDs and CDs (VCD, sVCD or CVD)

License:        GPLv3
URL:            http://www.rastersoft.com/programas/devede.html
Source0:        https://gitlab.com/rastersoft/devedeng/-/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

Provides:       devede = %{version}-%{release}
Obsoletes:      devede < 4.0

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
#Requires:       (vlc or mpv or mplayer)
Requires:       vlc
Requires:       ffmpeg
Requires:       dvdauthor
Requires:       vcdimager
Requires:       genisoimage
#Requires:       (brasero or k3b or xfburn)
Requires:       brasero
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
%autosetup -p1 -n %{name}-%{version}


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

# Fix AppData file
mv %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml \
  %{buildroot}%{_datadir}/metainfo/devede_ng.py.appdata.xml
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
* Sat Feb 03 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 4.17.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Aug 05 2023 Leigh Scott <leigh123linux@gmail.com> - 4.17.0-6
- Drop patch

* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 4.17.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 08 2023 Leigh Scott <leigh123linux@gmail.com> - 4.17.0-4
- Rebuilt for Python 3.12

* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 4.17.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Sat Jun 25 2022 Robert-André Mauchin <zebob.m@gmail.com> - 4.17.0-2
- Rebuilt for Python 3.11

* Sat Mar 05 2022 Andrea Musuruane <musuruan@gmail.com> - 4.17.0-1
- Updated to new upstream release

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 4.16.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 02 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 4.16.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 15 2021 Leigh Scott <leigh123linux@gmail.com> - 4.16.0-9
- Rebuild for python-3.10

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 4.16.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan  6 10:20:42 CET 2021 Andrea Musuruane <musuruan@gmail.com> - 4.16.0-7
- Reverted the use of boolean operators in Requires (BZ #5879)

* Sat Jan  2 16:28:31 CET 2021 Andrea Musuruane <musuruan@gmail.com> - 4.16.0-6
- Reverted the use of boolean operators in Requires (BZ #5879)

* Mon Dec 28 13:32:51 CET 2020 Andrea Musuruane <musuruan@gmail.com> - 4.16.0-5
- Used boolean operators in Requires (BZ #5879)

* Mon Aug 17 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 4.16.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 30 2020 Leigh Scott <leigh123linux@gmail.com> - 4.16.0-3
- Rebuild for python-3.9

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 4.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 20 2019 Andrea Musuruane <musuruan@gmail.com> - 4.16.0-1
- Updated to new upstream release
- Changed license to GPLv3 only

* Sat Aug 24 2019 Leigh Scott <leigh123linux@gmail.com> - 4.15.0-3
- Rebuild for python-3.8

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 4.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 27 2019 Nicolas Chauvet <kwizart@gmail.com> - 4.15.0-1
- Update to 4.15.0

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 4.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Feb 08 2019 Andrea Musuruane <musuruan@gmail.com> - 4.14.0-1
- Updated to new upstream release

* Fri Feb 01 2019 Andrea Musuruane <musuruan@gmail.com> - 4.13.0-1
- Updated to new upstream release

* Sun Sep 30 2018 Leigh Scott <leigh123linux@googlemail.com> - 4.12.0-4
- Require genisoimage as mkisofs virtual provides was removed

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 4.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

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

