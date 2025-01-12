
template_class = \
"""//
// Copyright (C) 2020 Signal Messenger, LLC.
// All rights reserved.
//
// SPDX-License-Identifier: GPL-3.0-only
//

// Generated by zkgroup/codegen/codegen.py - do not edit

package org.signal.zkgroup%(dir_section)s;

%(imports)s

public final class %(class_name)s extends ByteArray {

  public static final int SIZE = %(size)s;
%(static_methods)s%(constructors)s
%(methods)s%(serialize_method)s}
"""

template_constructor = \
"""
  %(constructor_access)s %(class_name)s(%(constructor_contents_type)s contents) %(constructor_exception_decl)s {
    super(%(constructor_contents)s, SIZE%(runtime_error_bool)s);%(check_valid_contents)s
  }
"""

template_constructor_for_string_contents = \
"""
  %(constructor_access)s %(class_name)s(%(constructor_contents_type)s contents) %(constructor_exception_decl)s {
    super(%(constructor_contents)s, SIZE%(runtime_error_bool)s);%(check_valid_contents)s
  }
"""

serialize_method_string = \
"""
  public String serialize() {
    try {
      return new String(contents, "UTF-8");
    } catch (UnsupportedEncodingException e) {
      throw new AssertionError();
    }
  }

"""

serialize_method_binary = \
"""
  public byte[] serialize() {
    return contents.clone();
  }

"""

template_wrapping_class = \
"""//
// Copyright (C) 2020 Signal Messenger, LLC.
// All rights reserved.
//
// SPDX-License-Identifier: GPL-3.0-only
//

// Generated by zkgroup/codegen/codegen.py - do not edit

package org.signal.zkgroup%(dir_section)s;

%(imports)s

public class %(class_name)s {

  private final %(wrapped_class_type)s %(wrapped_class_var)s;
%(static_methods)s
  public %(class_name)s(%(wrapped_class_type)s %(wrapped_class_var)s) {
    this.%(wrapped_class_var)s = %(wrapped_class_var)s;
  }
%(methods)s
}
"""

template_check_valid_contents_constructor = \
"""
    
    int ffi_return = Native.%(class_name_lower_camel)sCheckValidContentsJNI(contents);

    if (ffi_return == Native.FFI_RETURN_INPUT_ERROR) {
      throw new InvalidInputException("FFI_RETURN_INPUT_ERROR");
    }

    if (ffi_return != Native.FFI_RETURN_OK) {
      throw new ZkGroupError("FFI_RETURN!=OK");
    }"""

template_check_valid_contents_constructor_runtime_error = \
"""
    
    int ffi_return = Native.%(class_name_lower_camel)sCheckValidContentsJNI(contents);

    if (ffi_return == Native.FFI_RETURN_INPUT_ERROR) {
      throw new IllegalArgumentException(new InvalidInputException("FFI_RETURN_INPUT_ERROR"));
    }

    if (ffi_return != Native.FFI_RETURN_OK) {
      throw new ZkGroupError("FFI_RETURN!=OK");
    }"""

template_static_method = \
"""
  %(access)s static %(return_name)s %(method_name)s(%(param_decls)s) %(exception_decl)s{
    byte[] newContents = new byte[%(return_name)s.SIZE];%(get_rand)s

    int ffi_return = Native.%(jni_method_name)s(%(param_args)snewContents);%(exception_check)s

    if (ffi_return != Native.FFI_RETURN_OK) {
      throw new ZkGroupError("FFI_RETURN!=OK");
    }

    try {
      return new %(return_name)s(newContents);
    } catch (InvalidInputException e) {
      throw new AssertionError(e);
    }
  }
"""

template_static_method_retval_runtime_error_on_serialize = \
"""
  %(access)s static %(return_name)s %(method_name)s(%(param_decls)s) %(exception_decl)s{
    byte[] newContents = new byte[%(return_name)s.SIZE];%(get_rand)s

    int ffi_return = Native.%(jni_method_name)s(%(param_args)snewContents);%(exception_check)s

    if (ffi_return != Native.FFI_RETURN_OK) {
      throw new ZkGroupError("FFI_RETURN!=OK");
    }

    try {
      return new %(return_name)s(newContents);
    } catch (IllegalArgumentException e) {
      throw new AssertionError(e);
    } 
  }
"""

template_static_method_rand_wrapper = \
"""
  %(access)s static %(return_name)s %(method_name)s(%(param_decls)s) %(exception_decl)s{
    return %(full_method_name)s(%(param_args)s);
  }
"""

template_method = \
"""
  %(access)s %(return_name)s %(method_name)s(%(param_decls)s) %(exception_decl)s{
    byte[] newContents = new byte[%(return_len)s];%(get_rand)s

    int ffi_return = Native.%(jni_method_name)s(%(contents)s, %(param_args)snewContents);%(exception_check)s

    if (ffi_return != Native.FFI_RETURN_OK) {
      throw new ZkGroupError("FFI_RETURN!=OK");
    }

    try {
      return new %(return_name)s(newContents);
    } catch (InvalidInputException e) {
      throw new AssertionError(e);
    }

  }
"""

template_method_retval_runtime_error_on_serialize = \
"""
  %(access)s %(return_name)s %(method_name)s(%(param_decls)s) %(exception_decl)s{
    byte[] newContents = new byte[%(return_len)s];%(get_rand)s

    int ffi_return = Native.%(jni_method_name)s(%(contents)s, %(param_args)snewContents);%(exception_check)s

    if (ffi_return != Native.FFI_RETURN_OK) {
      throw new ZkGroupError("FFI_RETURN!=OK");
    }

    return new %(return_name)s(newContents);
  }
"""

template_method_bool = \
"""
  %(access)s void %(method_name)s(%(param_decls)s) %(exception_decl)s{
    int ffi_return = Native.%(jni_method_name)s(%(contents)s, %(param_args)s);%(exception_check)s

    if (ffi_return != Native.FFI_RETURN_OK) {
      throw new ZkGroupError("FFI_RETURN!=OK");
    }
  }
"""

template_method_uuid = \
"""
  %(access)s UUID %(method_name)s(%(param_decls)s) %(exception_decl)s{
    byte[] newContents = new byte[%(return_len)s];

    int ffi_return = Native.%(jni_method_name)s(%(contents)s, %(param_args)snewContents);%(exception_check)s

    if (ffi_return != Native.FFI_RETURN_OK) {
      throw new ZkGroupError("FFI_RETURN!=OK");
    }

    return UUIDUtil.deserialize(newContents);
  }
"""

template_method_bytearray = \
"""
  %(access)s byte[] %(method_name)s(%(param_decls)s) %(exception_decl)s{
    byte[] newContents = new byte[%(return_len)s];%(get_rand)s

    int ffi_return = Native.%(jni_method_name)s(%(contents)s, %(param_args)snewContents);%(exception_check)s

    if (ffi_return != Native.FFI_RETURN_OK) {
      throw new ZkGroupError("FFI_RETURN!=OK");
    }

    return newContents;
  }
"""

template_method_int = \
"""
  %(access)s int %(method_name)s(%(param_decls)s) %(exception_decl)s{
    byte[] newContents = new byte[4];

    int ffi_return = Native.%(jni_method_name)s(%(contents)s, %(param_args)snewContents);%(exception_check)s

    if (ffi_return != Native.FFI_RETURN_OK) {
      throw new ZkGroupError("FFI_RETURN!=OK");
     }

    return ByteBuffer.wrap(newContents).getInt();
  }
"""

template_method_long = \
"""
  %(access)s long %(method_name)s(%(param_decls)s) %(exception_decl)s{
    byte[] newContents = new byte[8];

    int ffi_return = Native.%(jni_method_name)s(%(contents)s, %(param_args)snewContents);%(exception_check)s

    if (ffi_return != Native.FFI_RETURN_OK) {
      throw new ZkGroupError("FFI_RETURN!=OK");
    }

    return ByteBuffer.wrap(newContents).getLong();
  }
"""

template_method_rand_wrapper = \
"""
  public %(return_name)s %(method_name)s(%(param_decls)s) %(exception_decl)s{
    return %(full_method_name)s(%(param_args)s);
  }
"""


template_native = \
"""//
// Copyright (C) 2020 Signal Messenger, LLC.
// All rights reserved.
//
// SPDX-License-Identifier: GPL-3.0-only
//

// Generated by zkgroup/codegen/codegen.py - do not edit

package org.signal.zkgroup.internal;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.nio.file.Files;

public final class Native {

  public static final int FFI_RETURN_OK             = 0;
  public static final int FFI_RETURN_INTERNAL_ERROR = 1; // ZkGroupError
  public static final int FFI_RETURN_INPUT_ERROR    = 2;

  public static final int RANDOM_LENGTH = 32;

  static {
    try {
      String  osName    = System.getProperty("os.name").toLowerCase(java.util.Locale.ROOT);
      boolean isMacOs   = osName.startsWith("mac os x");
      String  extension = isMacOs ? ".dylib" : ".so";

      try (InputStream in = Native.class.getResourceAsStream("/libzkgroup" + extension)) {
        if (in != null) {
          copyToTempFileAndLoad(in, extension);
        } else {
          System.loadLibrary("zkgroup");
        }
      }
    } catch (Exception e) {
      throw new RuntimeException(e);
    }
  }

  private Native() {
  }

  private static void copyToTempFileAndLoad(InputStream in, String extension) throws IOException {
    File tempFile = Files.createTempFile("resource", extension).toFile();
    tempFile.deleteOnExit();

    try (OutputStream out = new FileOutputStream(tempFile)) {

      copy(in, out);
    }
    System.load(tempFile.getAbsolutePath());
  }

"""        

template_native_end = \
"""
  private static void copy(InputStream in, OutputStream out) throws IOException {
    byte[] buffer = new byte[4096];
    int read;

    while ((read = in.read(buffer)) != -1) {
      out.write(buffer, 0, read);
    }
  }
}
"""

native_string = template_native

def add_import(import_strings, class_dir_dict, my_dir_name, class_name):
    dir_name = class_dir_dict[class_name.snake()].snake()
    if len(dir_name)==0 and len(my_dir_name.snake()) == 0:
        return
    elif dir_name == my_dir_name.snake():
        return
    if dir_name:
        import_strings.append("import org.signal.zkgroup.%s.%s;" % (dir_name, class_name.camel()))
    else:
        import_strings.append("import org.signal.zkgroup.%s;" % (class_name.camel()))

def get_decls(params, import_strings, class_dir_dict, my_dir_name):
    s = ""
    for param in params:
        if param[1].snake() == "randomness":
            s += "SecureRandom secureRandom, "
            import_strings.append("import java.security.SecureRandom;")
        elif param[0] == "class":
            s += param[1].camel() + " " + param[1].lower_camel() + ", "
            add_import(import_strings, class_dir_dict, my_dir_name, param[1])
        else:
            s += param[0] + " " + param[1].lower_camel() + ", "
    if len(s) != 0:
        s = s[:-2]
    return s

def get_rand_wrapper_decls(params):
    s = ""
    for param in params:
        if param[1].snake() != "randomness":
            if param[0] == "class":
                s += param[1].camel() + " " + param[1].lower_camel() + ", "
            else:
                s += param[0] + " " + param[1].lower_camel() + ", "
    if len(s) != 0:
        s = s[:-2]
    return s


def get_args(params, import_strings, commaAtEnd):
    s = ""
    for param in params:
        if param[0] == "byte[]" or param[0] == "int" or param[0] == "long":
            s += param[1].lower_camel() + ", "
        elif param[0] == "UUID":
            s += "UUIDUtil.serialize(" + param[1].lower_camel() + "), "
            import_strings.append("import java.util.UUID;")
            import_strings.append("import org.signal.zkgroup.util.UUIDUtil;")
        elif param[1].snake() == "randomness":
            s += "random, "
        else:
            s += param[1].lower_camel() + ".getInternalContentsForJNI(), "

    if len(s) != 0 and not commaAtEnd:
        s = s[:-2]
    return s

def get_jni_arg_decls(params, selfBool, commaAtEndBool):
    s = ""
    if selfBool:
        s += "byte[] self, "
    counter = 0
    for param in params:
        if param[0] == "int":
            s += f"int {param[1].lower_camel()}, "
        elif param[0] == "long":
            s += f"long {param[1].lower_camel()}, "
        else:
            s += f"byte[] {param[1].lower_camel()}, "
        counter += 1

    if len(s) != 0 and not commaAtEndBool:
        s = s[:-2]

    if commaAtEndBool:
        s += "byte[] output"

    return s

def get_rand_wrapper_args(params, commaAtEnd):
    s = ""
    for param in params:
        if param[0] == "byte[]":
            s += param[1].lower_camel() + ", "
        elif param[1].snake() == "randomness":
            s += "new SecureRandom(), "
        else:
            s += param[1].lower_camel() + ", "
    if len(s) != 0 and not commaAtEnd:
        s = s[:-2]
    return s

def append_jni_function_decl(jni_method_name, params, selfBool, commaAtEndBool):
    global native_string
    native_string += "  public static native int " + jni_method_name + "(%s);\n" % get_jni_arg_decls(params, selfBool, commaAtEndBool)

def append_jni_check_valid_contents(jni_method_name):
    global native_string
    native_string += "  public static native int " + jni_method_name + "(byte[] self);\n"

def print_class(c, runtime_error_on_serialize_dict, class_dir_dict):
    static_methods_string = ""
    if len(c.methods) == 0 and len(c.static_methods) == 0:
        import_strings = []
    else:
        import_strings = [\
"import org.signal.zkgroup.internal.Native;",
            ]

    global native_string
    my_dir_name = c.dir_name

    if c.wrap_class == None:
        contents = "contents"
    else:
        contents = c.wrap_class.lower_camel() + ".getInternalContentsForJNI()"
        add_import(import_strings, class_dir_dict, my_dir_name, c.wrap_class)

    for method in c.static_methods:

        exception_decl = ""
        exception_check =""
        if len(method.params) > 1 or (len(method.params) == 1 and not method.method_name.snake().endswith("_deterministic")):
            if method.runtime_error == False:
                if method.verification == False:
                    if my_dir_name.snake() != "":
                        import_strings.append("import org.signal.zkgroup.VerificationFailedException;")
                    exception_decl = "throws VerificationFailedException "
                    exception_check ="""\n    if (ffi_return == Native.FFI_RETURN_INPUT_ERROR) {
      throw new VerificationFailedException();
    }"""
                else:
                    exception_decl = "throws VerificationFailedException "
                    exception_check ="""\n    if (ffi_return == Native.FFI_RETURN_VERIFICATION_FAILED) {
      throw new VerificationFailedException();
    }"""

        access = "public"
        method_name = method.method_name.lower_camel()
        get_rand = ""
        if method.method_name.snake().endswith("_deterministic"):
            import_strings.append("import java.security.SecureRandom;")
            method_name = method.method_name.lower_camel()[:-len("Deterministic")]
            param_args = get_rand_wrapper_args(method.params, False)
            get_rand = """\n    byte[] random      = new byte[Native.RANDOM_LENGTH];

    secureRandom.nextBytes(random);"""
            static_methods_string += template_static_method_rand_wrapper % {
                    "method_name": method_name,
                    "return_name": method.return_name.camel(),
                    "full_method_name": method_name,
                    "param_decls": get_rand_wrapper_decls(method.params),
                    "param_args": param_args,
                    "access": access,
                    "exception_decl": exception_decl,
                    "exception_check": exception_check,
                    }
        param_args = get_args(method.params, import_strings, True)
        if c.wrap_class == None:
            jni_method_name = c.class_name.lower_camel() + method.method_name.camel() + "JNI"
        else:
            jni_method_name = c.wrap_class.lower_camel()  + method.method_name.camel() + "JNI"
        append_jni_function_decl(jni_method_name, method.params, False, True)
        if runtime_error_on_serialize_dict[method.return_name.snake()]:
            template = template_static_method_retval_runtime_error_on_serialize
            import_strings.append("import org.signal.zkgroup.ZkGroupError;")
        else:
            template = template_static_method
            if my_dir_name.snake() != "":
                import_strings.append("import org.signal.zkgroup.InvalidInputException;")
        static_methods_string += template % {
                "method_name": method_name,
                "return_name": method.return_name.camel(),
                "return_len": c.class_len,
                "param_decls": get_decls(method.params, import_strings, class_dir_dict, my_dir_name),
                "param_args": param_args,
                "jni_method_name": jni_method_name, 
                "access": access,
                "exception_decl": exception_decl,
                "exception_check": exception_check,
                "get_rand": get_rand,
                }

    methods_string = ""
    for method in c.methods:

        if method.method_name.snake() == "check_valid_contents":
            continue

        exception_decl = ""
        exception_check =""
        if len(method.params) != 0:
            if method.runtime_error == False:
                if method.verification == False:
                    if my_dir_name.snake() != "":
                        import_strings.append("import org.signal.zkgroup.VerificationFailedException;")
                    exception_decl = "throws VerificationFailedException "
                    exception_check ="""\n    if (ffi_return == Native.FFI_RETURN_INPUT_ERROR) {
      throw new VerificationFailedException();
    }"""
                else:
                    exception_decl = "throws VerificationFailedException "
                    exception_check ="""\n    if (ffi_return == Native.FFI_RETURN_VERIFICATION_FAILED) {
      throw new VerificationFailedException();
    }"""

        access = "public"
        method_name = method.method_name.lower_camel()
        get_rand = ""
        if method.method_name.snake().endswith("_deterministic"):
            import_strings.append("import java.security.SecureRandom;")
            method_name = method.method_name.lower_camel()[:-len("Deterministic")]
            param_args = get_rand_wrapper_args(method.params, False)
            get_rand = """\n    byte[] random      = new byte[Native.RANDOM_LENGTH];

    secureRandom.nextBytes(random);"""

            # Maybe add more cases to support different return types
            if method.return_type == "byte[]":
                return_name = "byte[]"
            else:
                return_name = method.return_name.camel()

            methods_string += template_method_rand_wrapper % {
                    "contents": contents,
                    "method_name": method_name,
                    "return_name": return_name,
                    "full_method_name": method_name,
                    "param_decls": get_rand_wrapper_decls(method.params),
                    "param_args": param_args,
                    "access": access,
                    "exception_decl": exception_decl,
                    "exception_check": exception_check,
                    }

        if c.wrap_class == None:
            jni_method_name = c.class_name.lower_camel() + method.method_name.camel() + "JNI"
        else:
            jni_method_name = c.wrap_class.lower_camel()  + method.method_name.camel() + "JNI"

        return_len = None
        if method.return_type == "boolean":
            template = template_method_bool
            param_args = get_args(method.params, import_strings, False)
            append_jni_function_decl(jni_method_name, method.params, True, False)
        elif method.return_type == "int":
            template = template_method_int
            param_args = get_args(method.params, import_strings, False)
            append_jni_function_decl(jni_method_name, method.params, True, True)
            import_strings += "import java.nio.ByteBuffer;",
        elif method.return_type == "long":
            template = template_method_long
            param_args = get_args(method.params, import_strings, False)
            append_jni_function_decl(jni_method_name, method.params, True, True)
            import_strings += "import java.nio.ByteBuffer;",
        elif method.return_type == "UUID":
            import_strings.append("import java.util.UUID;")
            template = template_method_uuid
            param_args = get_args(method.params, import_strings, True)
            append_jni_function_decl(jni_method_name, method.params, True, True)
        elif method.return_type == "byte[]": # copied from UUID?
            template = template_method_bytearray
            param_args = get_args(method.params, import_strings, True)
            append_jni_function_decl(jni_method_name, method.params, True, True)
            if method.relative_return_size is not None:
                return_len = f"{method.params[method.relative_return_size][1].lower_camel()}.length + {method.return_size_increment}"
        else:
            add_import(import_strings, class_dir_dict, my_dir_name, method.return_name)
            if runtime_error_on_serialize_dict[method.return_name.snake()]:
                template = template_method_retval_runtime_error_on_serialize
            else:
                template = template_method
                import_strings.append("import org.signal.zkgroup.ZkGroupError;")
            param_args = get_args(method.params, import_strings, True)
            append_jni_function_decl(jni_method_name, method.params, True, True)
        if method.return_name.snake() == "uuid":
            return_len = "UUIDUtil.UUID_LENGTH"
        elif return_len is None:
            return_len = method.return_name.camel() + ".SIZE"


        methods_string += template % {
                "contents": contents,
                "method_name": method_name,
                "return_name": method.return_name.camel(),
                "return_len": return_len,
                "param_decls": get_decls(method.params, import_strings, class_dir_dict, my_dir_name),
                "param_args": param_args,
                "jni_method_name": jni_method_name, 
                "access": access,
                "exception_decl": exception_decl,
                "exception_check": exception_check,
                "get_rand": get_rand,
                }

    if c.dir_name.snake() != "":
        dir_section = "." + c.dir_name.snake()
    else:
        dir_section = ""

    constructor_exception_decl = "throws InvalidInputException" # overwritten in needed
    runtime_error_bool = ""
    if c.check_valid_contents:
        if c.runtime_error_on_serialize:
            constructor_exception_decl = "" # overwritten in needed
            runtime_error_bool = ", true"
            check_valid_contents = template_check_valid_contents_constructor_runtime_error % {
                    "class_name_lower_camel": c.class_name.lower_camel(), 
                    }
            jni_method_name = c.class_name.lower_camel() + "CheckValidContentsJNI"
            append_jni_check_valid_contents(jni_method_name)
            if my_dir_name.snake() != "":
                import_strings.append("import org.signal.zkgroup.ZkGroupError;")
                import_strings.append("import org.signal.zkgroup.InvalidInputException;")
        else:
            constructor_exception_decl = "throws InvalidInputException" # overwritten in needed
            check_valid_contents = template_check_valid_contents_constructor % {
                    "class_name_lower_camel": c.class_name.lower_camel(), 
                    }
            jni_method_name = c.class_name.lower_camel() + "CheckValidContentsJNI"
            append_jni_check_valid_contents(jni_method_name)
            if my_dir_name.snake() != "":
                import_strings.append("import org.signal.zkgroup.InvalidInputException;")
                import_strings.append("import org.signal.zkgroup.ZkGroupError;")
    else:
        check_valid_contents = ""

    if constructor_exception_decl.endswith("InvalidInputException") and my_dir_name.snake() != "":
        import_strings.append("import org.signal.zkgroup.InvalidInputException;")

    if c.no_serialize:
        constructor_access = "private"
    else:
        constructor_access = "public"

    if c.wrap_class == None:
        import_strings.append("import org.signal.zkgroup.internal.ByteArray;")
    import_strings = list(set(import_strings))
    import_strings.sort()

    # constructors
    constructors_string = ""
    constructor_contents = "contents"
    constructor_contents_type = "byte[]"
    constructors_string += template_constructor % {
        "class_name": c.class_name.camel(), 
        "constructor_contents": constructor_contents,
        "constructor_contents_type": constructor_contents_type,
        "constructor_access": constructor_access,
        "constructor_exception_decl": constructor_exception_decl,
        "runtime_error_bool": runtime_error_bool,
        "check_valid_contents": check_valid_contents,
        }

    if c.string_contents == False:
        serialize_method = serialize_method_binary
    else:
        constructor_contents = 'contents.getBytes("UTF-8")'
        constructor_contents_type = "String"
        import_strings.append("import java.io.UnsupportedEncodingException;")
        serialize_method = serialize_method_string
        constructors_string += template_constructor_for_string_contents % {
            "class_name": c.class_name.camel(), 
            "constructor_contents": constructor_contents,
            "constructor_contents_type": constructor_contents_type,
            "constructor_access": constructor_access,
            "constructor_exception_decl": constructor_exception_decl + ", UnsupportedEncodingException",
            "runtime_error_bool": runtime_error_bool,
            "check_valid_contents": check_valid_contents,
            }
    constructors_string = constructors_string[:-1]

    if c.wrap_class != None:
        class_string = template_wrapping_class % {
                "imports": "\n".join(import_strings),
                "wrapped_class_type": c.wrap_class.camel(),
                "wrapped_class_var": c.wrap_class.lower_camel(), 
                "dir_section": dir_section,
                "class_name": c.class_name.camel(), 
                "size": c.class_len_int,
                "constructors": constructors_string,
                "static_methods": static_methods_string,
                "methods": methods_string,
                "serialize_method": serialize_method
                }
    else:
        class_string = template_class % {
                "imports": "\n".join(import_strings),
                "dir_section": dir_section,
                "class_name": c.class_name.camel(), 
                "size": c.class_len_int,
                "constructors": constructors_string,
                "static_methods": static_methods_string,
                "methods": methods_string,
                "serialize_method": serialize_method
                }
    return class_string


def produce_output(classes):

    runtime_error_on_serialize_dict = {}
    class_dir_dict = {}
    for c in classes:
        runtime_error_on_serialize_dict[c.class_name.snake()] = c.runtime_error_on_serialize
        class_dir_dict[c.class_name.snake()] = c.dir_name

    for c in classes:
        if c.no_class:
            continue
        if c.dir_name.snake() != "":
            f = open("java/%s/%s.java" % (c.dir_name.snake(), c.class_name.camel()), "w")
        else:
            f = open("java/%s.java" % c.class_name.camel(), "w")
        f.write(print_class(c, runtime_error_on_serialize_dict, class_dir_dict))
        f.close()
    f = open("java/internal/Native.java", "w")
    global native_string
    native_string += template_native_end
    f.write(native_string)
    f.close()
