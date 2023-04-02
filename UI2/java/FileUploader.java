import java.io.File;
import java.io.IOException;
import java.nio.file.Files;

import org.apache.commons.io.FileUtils;
import org.springframework.web.multipart.MultipartFile;

public class FileUploader {
	
	//Non compliant - file extensions not mentioned, file extensions not validated, 
	//upload file size is not mentioned, upload file size is not validated	
	
    public static void uploadImage(MultipartFile imageFile) throws IOException {
        String fileName = imageFile.getOriginalFilename();
		
		
        byte[] bytes = imageFile.getBytes();
		
		
		//private static final List<String> IMAGE_EXTENSIONS = Arrays.asList("jpg", "jpeg", "png", "gif");
		
		
        File file = new File("C:/uploads/images/" + fileName);
        FileUtils.writeByteArrayToFile(file, bytes);
    }
	
	
    
    //Non compliant - file extensions not mentioned, validated.
    public static void uploadFile(MultipartFile uploadedFile) throws IOException {
        String fileName = uploadedFile.getOriginalFilename();
		
        byte[] bytes = uploadedFile.getBytes();
		
		
		//private static final List<String> FILE_EXTENSIONS = Arrays.asList("pdf", "doc", "docx", "xls", "xlsx");
		
		
		
		
        File file = new File("C:/uploads/files/" + fileName);
        FileUtils.writeByteArrayToFile(file, bytes);
    }
}


