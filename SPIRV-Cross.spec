%global sdkver 1.4.304.0

Name:           SPIRV-Cross
Version:        0.0.1
Release:        %autorelease
Summary:        A tool designed for parsing and converting SPIR-V to other shader languages.

License:        BSD-2-Clause AND BSD-3-Clause AND GPL-3.0-or-later AND Apache-2.0
URL:            https://github.com/KhronosGroup/%{name}
Source0:        %url/archive/vulkan-sdk-%{sdkver}.tar.gz#/%{name}-sdk-%{sdkver}.tar.gz

BuildRequires:  cmake3
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
# BuildRequires:  spirv-tools-devel

%description
SPIRV-Cross is a practical tool and library for performing reflection on SPIR-V
and disassembling SPIR-V back to high level languages. 
SPIRV-Cross tries hard to emit readable and clean output from the SPIR-V. The
goal is to emit GLSL or MSL that looks like it was written by a human and not
awkward IR/assembly-like code.

# %package        devel
# Summary:        Development files for %{name}
# Requires:       %{name}%{?_isa} = %{version}-%{release}

# %description    devel

%prep
%autosetup -p1 -n %{name}-vulkan-sdk-%{sdkver}
# Fix rpmlint warning on debuginfo
# find . -name '*.h' -or -name '*.cpp' -or -name '*.hpp'| xargs chmod a-x

%build
%cmake3 -DSPIRV_CROSS_SHARED=ON
%cmake_build

%install
%{cmake_install}
rm -r %{buildroot}/%{_datadir}


# %check

%files
%doc README.md
%{_bindir}/%{lower:%{name}}
%{_libdir}/libspirv-cross-c-shared.so*
%{_libdir}/libspirv-cross-{c,core,cpp,glsl,hlsl,msl,reflect,util}.a
%{_libdir}/pkgconfig/spirv-cross-c{,-shared}.pc
%{_includedir}/spirv_cross/

# %files devel

%changelog
%autochangelog
