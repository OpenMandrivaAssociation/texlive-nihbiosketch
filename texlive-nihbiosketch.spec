%global tl_name nihbiosketch
%global tl_revision 78482

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A class for NIH biosketches based on the 2015 updated format
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/nihbiosketch
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nihbiosketch.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nihbiosketch.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This LaTeX document class tries to adhere to the Biographical Sketch
formatting requirements outlined in NIH Notice [NOT-OD-15-032]
(http://grants.nih.gov/grants/guide/notice-files/NOT-OD-15-032. html).
This new format is required for applications submitted for due dates on
or after May 25, 2015. The package tries to mimic the example documents
provided on the [SF 424 (R&R) Forms and Applications page]
(http://grants.nih.gov/grants/funding/424/index.htm#format) as closely
as possible. The author has used this class for his own grant
submissions; however he offers no guarantee of conformity to NIH
requirements.

